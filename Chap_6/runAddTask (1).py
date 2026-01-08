import addTask

if __name__ == '__main__':
    result = addTask.add.delay(5, 5)
    print(f"Task ID: {result.id}")
    print(f"Task Status: {result.status}")
    print(f"Task Result: {result.get(timeout=10)}")