#!python3

from googletrans import Translator as GTrans

if __name__ == "__main__":
    gtrans = GTrans()
    result = gtrans.detect("Hello! How can I assist you?")
    print(result.lang)
