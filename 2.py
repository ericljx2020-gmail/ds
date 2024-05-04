def brackets(s):
    st = []
    res = [" " for _ in range(len(s))]
    ans = s+"\n"
    for i in range(len(s)):
        c = s[i]
        if c != '(' and c != ')':
            continue                # let it place be " "
        elif c == '(':
            st.append(i)
            res[i] = 'x'
        elif c == ')':
            if len(st) != 0:
                res[st[-1]] = ' '       #如果匹配上了则给回 “ ”
                res[i] = " "
                st.pop()
            else:
                res[i] = "?"
    for c in res:
        ans += c
    return ans

s = "))))UUUU((()"
result = brackets(s)
print(result)   