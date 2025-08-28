from persister.src.consumer_manager import ConsumerManager


def main():
    manager = ConsumerManager()
    manager.consumer_to_mongodb()

if __name__ == '__main__':
    main()