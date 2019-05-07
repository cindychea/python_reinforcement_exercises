documentary = 'Becoming Warren Buffett'
drama = 'Black Panther'
comedy = 'The Mask'
dramedy = 'Silver Linings Playbook'

print("Do you like documentaries?")
likes_docs = input()
print("Do you like dramas?")
likes_dramas = input()
print("Do you like comedies?")
likes_comedies = input()

if likes_docs == 'yes' or likes_docs == 'y':
    print("You should watch {}.".format(documentary))
elif (likes_comedies == 'yes' or likes_comedies == 'y') and (likes_dramas == 'yes' or likes_dramas == 'y'):
    print("You should watch {}.".format(dramedy))
elif likes_dramas == 'yes' or likes_dramas == 'y':
    print("You should watch {}.".format(drama))
elif likes_comedies == 'yes' or likes_comedies == 'y':
    print("You should watch {}.".format(comedy))
else:
    print("You should read The Book of M by Peng Shepherd.")