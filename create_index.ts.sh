#!/bin/bash
# Creates an index.ts with exports of all .ts files in that directory

rm index.ts 2> /dev/null

for file in *.ts;
do
    [[ $file =~ \.test\.ts$ ]] && continue

    echo "export * from './$file';" >> index.ts
done

cat index.ts