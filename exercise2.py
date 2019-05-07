documentary = 'Becoming Warren Buffett'
drama = 'Black Panther'
comedy = 'The Mask'
dramedy = 'Silver Linings Playbook'

print("Rate your appreciation for documentaries from 1-5.")
rating_docs = int(input())
print("Rate your appreciation for dramas from 1-5.")
rating_dramas = int(input())
print("Rate your appreciation for comedies from 1-5.")
rating_comedies = int(input())

if rating_docs >= 4:
    print("You should watch {}.".format(documentary))
elif rating_docs <= 3 and rating_comedies >= 4 and rating_dramas >= 4:
    print("You should watch {}.".format(dramedy))
elif rating_dramas >= 4:
    print("You should watch {}.".format(drama))
elif rating_comedies >= 4:
    print("You should watch {}.".format(comedy))
elif rating_docs <= 3 and rating_dramas <= 3 and rating_comedies <=3:
    
else:
    print("You should read The Book of M by Peng Shepherd.")