import argparse
from insert import *
from delete import *
from selectt import *
from order_by_size import *
from order_by_price import *



def add_(price, size):
    insert(price, size)


def delete_(id):
    delete(str(id))


def list_():
    selectt()


def sort_list_(sort_list):
    match sort_list:
        case 'size':
            order_by_size()
        case 'price':
            order_by_price()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("pos", choices=['list', 'delete', 'add'])
    parser.add_argument("add_values", nargs="*", type=int)
    parser.add_argument("-s", '--sort', choices=['price', 'size'])
    args = parser.parse_args()

    if args.pos == 'add':
        add_(price=args.add_values[0], size=args.add_values[1])

    if args.pos == 'delete':
        delete_(args.add_values[0])

    if args.pos == 'list':
        if args.sort == 'price' or args.sort == 'size':
            sort_list_(sort_list=args.sort)
        else:
            list_()


if __name__ == '__main__':
    main()