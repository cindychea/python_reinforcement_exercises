phrases = ["Totam", "ut", "odit","quis", "Maiores", "unde", "EX", "EST", "corporis"]

for (p=0; p < phrases.length; p++) {
    if (phrases[p].length > 4 && phrases[p] == phrases[p].toLowerCase()) {
        console.log('long and lowercase');
    } else if (phrases[p].length > 4) {
        console.log('long');
    } else if (phrases[p] == phrases[p].toLowerCase()) {
        console.log('lowercase');
    } else {
        console.log(phrases[p]);
    }
}