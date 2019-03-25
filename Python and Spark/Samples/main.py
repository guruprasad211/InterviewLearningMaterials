def main1():
    print("Hello from main")


# calling from python 3 onwards
main1()
print('Hello World outside main')
main1()

# calling using python 2
if __name__ == "__main__":
    print('calling from if condition')
    main1()
