# Enter your code here. Read input from STDIN. Print output to STDOUT
no = int(input())
word = []
words = []
for i in range(no):
    word = input()
    word = list(word)
    words.append(word)

for i in range(len(words)):
    first = []
    second = []
    for j in range(len(words[i])):
        if j % 2 ==0:
            first.append(words[i][j])
        else:
            second.append(words[i][j])
    f = ''.join(first)
    s = ''.join(second)
    print(f"{f} {s}")
  