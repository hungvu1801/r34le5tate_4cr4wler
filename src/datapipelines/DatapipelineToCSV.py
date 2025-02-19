from src.models.DataModel import DataModel
from dataclasses import fields, asdict
import time, os, csv

class DatapipelineToCSV:
    def __init__(self, data_queue_max=10, file_name=None):
        self.data_queue = []
        self.data_queue_max = data_queue_max
        self.file_name = file_name
        self.is_file_closed = True

    def save_to_csv(self) -> None:
        self.is_file_closed = False
        data_to_pushed = self.data_queue.copy()
        self.data_queue.clear()
        if not data_to_pushed:
            self.is_file_closed = True
            return
        keys = [field.name for field in fields(data_to_pushed[0])]
        with open(self.file_name, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            if not os.path.exists(self.file_name) or os.stat(self.file_name).st_size == 0:
                writer.writeheader()
            for data in data_to_pushed:
                writer.writerow(asdict(data))
        self.is_file_closed = True
        

    def add_data(self, scraped_data: dict) -> None:
        cleaned_data = DataModel(
            name=scraped_data['name'],
            type=scraped_data['type'],
            price=scraped_data['price'],
            size=scraped_data['size'],
            url_img=scraped_data['url_img'],
            place=scraped_data['place'],
            poster=scraped_data['poster'],
            url=scraped_data['url'],
            )
        self.data_queue.append(cleaned_data)
        if len(self.data_queue) >= self.data_queue_max and self.is_file_closed:
            self.save_to_csv()
    
    def close_pipeline(self) -> None:
        if not self.is_file_closed:
            time.sleep(10)

        if len(self.data_queue) > 0:
            self.save_to_csv()
