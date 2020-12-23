const sleep = require('system-sleep');
const e = require('ecoji-js');

function printProgressBar(iteration, total, prefix, suffix, fill) {

    // Write out the prefix
    process.stdout.write(prefix + " |");

    // Current progress using the fill character
    for (let i = 0; i < iteration; i++) {
        process.stdout.write(fill);
    }

    // Remaining progress using the "-" character
    for (let i = iteration; i < total; i++) {
        process.stdout.write('-');
    }

    // Write out the suffix
    process.stdout.write("| " + suffix);
    process.stdout.write('\r');
}

let emoji = e.encode("3").substring(0, 2);
for (let i = 0; i < 100; i++) {
    printProgressBar(i, 100, "Downloading", "Goal", emoji);
    sleep(25);
}
