import sys

def invertedstar(n):
    for i in range(n, 0, -1):
        print((n-i) * ' ' + i * '*')

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError('-1')
        n = int(sys.argv[1])
        if n < 1:
            raise ValueError('-1')
    except ValueError:
        print("\nPlease inform the desired number of lines. Example\n")
        print("Usage: python3 invertedstar.py <number of lines>\n")
        quit()
    
    invertedstar(n)