import coin

my_coin = coin.Coin()

print('This side is up:', my_coin.get_sideup())

for i in range(10):
    my_coin.toss()
    print(my_coin.get_sideup())
