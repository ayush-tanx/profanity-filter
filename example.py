from profanity_filter import ProfanityFilter

pf = ProfanityFilter()

k = pf.censor("Binance")
print(k)
# "********"
k = pf.censor("hello")
print(k)
# pf.censor_word('oofuko')
# # Word(uncensored='oofuko', censored='******', original_profane_word='fuck')

# pf.censor_whole_words = False
# pf.censor_word('h0r1h0r1')
# Word(uncensored='h0r1h0r1', censored='***1***1', original_profane_word='h0r')