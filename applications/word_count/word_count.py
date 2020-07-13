def word_count(s):
        # Your code here
        counts = {}

        fs = s.translate({ord(i): None for i in '":;,.-+=/\|[]{}()*^&'}).lower().split()
        # for c in s.lower().split():
        for c in fs:
            if c in counts:
                counts[c] +=1
            else:
                counts[c] = 1

        return counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))