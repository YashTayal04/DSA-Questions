def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A=int(input())
    dp=[0,1]
    for i in range(2,A+1):
        dp.append(dp[-1]+dp[-2])
    print(dp[A])
    return 0

if __name__ == '__main__':
    main()