const fs = require('fs');

fs.readFile('test-data/spaces.json', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }
    
    const jsonData = JSON.parse(data);

    let totalListsFound = 0;
    let testListsFound = 0;

    console.log(`\n======== Lists with names starting with "test": ========`);
    // Iterating through all folders and lists
    jsonData.folders.forEach(folder => {
        folder.lists.forEach((list) => {
            totalListsFound++;
            
            // If the list name starts with "test", output the space.name and space.id
            if (list.name.toLowerCase().startsWith('test')) {
                testListsFound++;
                console.log(`${testListsFound}. List ID: ${list.id}`);
                console.log('Space Name:', list.space.name);
                console.log('Space ID:', list.space.id);
            }
        });
    });

    console.log(`\n======== Summary ========`);
    console.log(`Total lists found: ${totalListsFound}`);
    console.log(`Lists with names starting with "test": ${testListsFound}`);
});

