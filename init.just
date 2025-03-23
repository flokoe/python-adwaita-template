init ID NAME AUTHOR:
    #!/usr/bin/bash

    name="{{ NAME }}"
    name_l="${name,}"
    name_u="${name^}"

    id="{{ ID }}"
    id_path="${id//.//}"

    find . -type f -name '*org.example.Turtur*' -exec rename -v org.example.Turtur {{ ID }} {} +
    find . -type f -name '*turtur*' -exec rename -v turtur "$name_l" {} +

    grep -rl --exclude=init.just 'org\.example\.Turtur' * | xargs sed -i 's/org\.example\.Turtur/{{ ID }}/g'
    grep -rl --exclude=init.just '/org/example/Turtur' * | xargs sed -i "s#/org/example/Turtur#$id_path#g"

    grep -rl --exclude=init.just turtur * | xargs sed -i "s/turtur/$name_l/g"
    grep -rl --exclude=init.just Turtur * | xargs sed -i "s/Turtur/$name_u/g"

    grep -rl --exclude=init.just AuthorName * | xargs sed -i 's/AuthorName/{{ AUTHOR }}/g'
