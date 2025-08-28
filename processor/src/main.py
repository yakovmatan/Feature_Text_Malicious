from processor.src.manager import Manager


if __name__ == '__main__':
    manager = Manager()
    manager.get_document_from_kafka_processing_and_publish_processed_document()