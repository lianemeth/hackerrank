st = raw_input()
st = st.lower()
chars = [ch for ch in st if ch.isalpha()]
if set(chars) == set('abcdefghijklmnopqrstuvwxyz'):
        print "pangram"
    else:
        print "not pangram"
