# Download youtube translations

You can download the youtube video translations with using this primitive script.

It uses [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api).

e.g. I use this to learn German.

## Install the requirements

```shell script
pip3 install -r ./requirements.txt
```

## Run the script

```shell script
python3 main.py 4-eDoThe6qo -l de -o nicos_weg.txt
```

### Download with translation

```shell script
python3 main.py 4-eDoThe6qo -l de -o nicos_weg.txt -t en
```

### Get available transcript list

```shell script
python3 main.py 4-eDoThe6qo -g
```
