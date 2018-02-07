def main():
    text = input("Please provide a sentence to reverse:\n")
    text_list = text.split()
    text_list.reverse()
    new_list = " ".join(text_list)
    print(new_list)

if __name__ == '__main__':
    main()
