This project creates a naive Bayesian classifier.
The training data is a csv wih 17 fields and 435 records.  The first field is a US House of Representatives member's party affiliation.  The rest are that representative's vote on pieces of legislation.  
The party affiliation is either democrat or republican.  Each legislation recieved a vote for (y),  vote against (n), or abstention (?).
The file bayes takes two arguments: the training data file and the classifying data file.
The program outputs the estimated probability that each record in classify is a democratic representative.  