# coding: utf-8
# created by liu hui


def main():

    def foo():
        from string_matching import KMP
        s = KMP("liu hui wei ru lei", "u")
        print(s)

    return foo


if __name__ == '__main__':
    main()()
