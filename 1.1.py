message = input(">Masukkan singkatan emoji = ")
singkatan = message.split(" ")
emojis_dict = {
    "TL"    : "😄",
    "TSGG"  : "🤣",
    "YKWIM" : "😏",
    "KGT"   : "😱",
    "HOAN"  : "🥱",
    "OKS"   : "👍",
    "MTB"   : "👏",
    "OTK"   : "🧠",
    "GBLK"  : "🙅",
    "IMS"   : "🦸",
    "SLMT"  : "🥳",
    "SMS"   : "🥺",
}

output = " "
for emoji in singkatan:
    output += emojis_dict.get(emoji, emoji) + " "

print(output)