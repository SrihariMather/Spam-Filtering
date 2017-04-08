def rbk(xmailer, clientSoftware, q):
    # clientSoftware = []
    d = 256
    M = len(clientSoftware)
    N = len(xmailer)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1
    flag = 0

    # The value of h would be "pow(d, M-1)%q"
    for i in xrange(M - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window
    # of text
    for i in xrange(M):
        p = (d * p + ord(clientSoftware[i])) % q
        t = (d * t + ord(xmailer[i])) % q

    print('Inside xmailer fn', xmailer)
    # Slide the pattern over text one by one
    for i in xrange(N - M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in xrange(M):
                if xmailer[i + j] != clientSoftware[j]:
                    break

            j += 1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == M:
                flag = 1
            else:
                flag = 0
                #print "Pattern found at index " + str(i)

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(xmailer[i]) * h) + ord(xmailer[i + M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q
    return flag