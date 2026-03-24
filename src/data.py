
# Danganronpa: Trigger Happy Havoc (DR1)
dr1_girls = [
    "Sayaka Maizono", "Junko Enoshima", "Toko Fukawa", "Aoi Asahina", 
    "Sakura Ogami", "Kyoko Kirigiri", "Celestia Ludenberg", "Mukuro Ikusaba"
]

# Danganronpa 2: Goodbye Despair (DR2)
dr2_girls = [
    "Akane Owari", "Chiaki Nanami", "Hiyoko Saionji", "Ibuky Mioda", 
    "Mahiru Koizumi", "Mikan Tsumiki", "Peko Pekoyama", "Sonia Nevermind"
]

# Danganronpa V3: Killing Harmony (DRV3)
drv3_girls = [
    "Kaede Akamatsu", "Angie Yonaga", "Himiko Yumeno", "Kirumi Tojo", 
    "Maki Harukawa", "Miu Iruma", "Tenko Chabashira", "Tsumugi Shirogane"
]

# Danganronpa Another Episode: Ultra Despair Girls (UDG)
udg_girls = [
    "Komaru Naegi", "Kotoko Utsugi", "Monaca Towa", "Hiroko Hagakure", "Kanon Nakajima"
]

all_danganronpa_girls = dr1_girls + dr2_girls + drv3_girls + udg_girls

# A dictionary of female characters from various anime and games
# TODO: Replace with JSON or SQLite
girls_characters_dict = {
    "Touhou" : [
    # --- PC-98 (TH01 - TH05) ---
    "Reimu Hakurei", "Singyoku (Female form)", "YuugenMagan", "Elis", "Sariel", "Mima", "Kikuri", "Konngara",
    "Genjii", "Rika", "Meira", "Marisa Kirisame", "Ellen", "Kotohime", "Kana Anaberal", "Rikako Asakura",
    "Chiyuri Kitashirakawa", "Yumemi Okazaki", "Orange", "Kurumi", "Elly", "Yuuka Kazami", "Mugetsu", "Gengetsu",
    "Sara", "Louise", "Alice Margatroid", "Yuki", "Mai", "Yumeko", "Shinki",

    # --- Windows (TH06 - TH09) ---
    "Rumia", "Daiyousei", "Cirno", "Hong Meiling", "Koakuma", "Patchouli Knowledge", "Sakuya Izayoi",
    "Remilia Scarlet", "Flandre Scarlet", "Letty Whiterock", "Chen", "Lily White", "Lunasa Prismriver",
    "Merlin Prismriver", "Lyrica Prismriver", "Youmu Konpaku", "Yuyuko Saigyouji", "Ran Yakumo", "Yukari Yakumo",
    "Suika Ibuki", "Wriggle Nightbug", "Mystia Lorelei", "Keine Kamishirasawa", "Tewi Inaba", 
    "Reisen Udongein Inaba", "Eirin Yagokoro", "Kaguya Houraisan", "Fujiwara no Mokou",

    # --- Windows (TH10 - TH13) ---
    "Aya Shameimaru", "Medicine Melancholy", "Komachi Onozuka", "Eiki Shiki, Yamaxanadu", "Shizuha Aki",
    "Minoriko Aki", "Hina Kagiyama", "Nitori Kawashiro", "Momiji Inubashiri", "Sanae Kochiya", "Kanako Yasaka",
    "Suwako Moriya", "Iku Nagae", "Tenshi Hinanawi", "Kisume", "Yamame Kurodani", "Parsee Mizuhashi",
    "Yuugi Hoshiguma", "Satori Komeiji", "Rin Kaenbyou", "Utsuho Reiuji", "Koishi Komeiji", "Nazrin",
    "Kogasa Tatara", "Ichirin Kumoi", "Minamitsu Murasa", "Shou Toramaru", "Byakuren Hijiri", "Nue Houjuu",
    "Hatate Himekaidou", "Kyouko Kasodani", "Yoshika Miyako", "Seiga Kaku", "Soga no Tojiko", "Mononobe no Futo",
    "Toyosatomimi no Miko", "Mamizou Futatsuiwa",

    # --- Windows (TH14 - TH19) ---
    "Hata no Kokoro", "Wakasagihime", "Sekibanki", "Kagerou Imaizumi", "Benben Tsukumo", "Yatsuhashi Tsukumo",
    "Seija Kijin", "Shinmyoumaru Sukuna", "Raiko Horikawa", "Sumireko Usami", "Seiran", "Ringo", "Doremy Sweet",
    "Sagume Kishin", "Clownpiece", "Junko", "Hecatia Lapislazuli", "Joon Yorigami", "Shion Yorigami",
    "Eternity Larva", "Nemuno Sakata", "Aunn Komano", "Narumi Yatadera", "Mai Teireida", "Satono Nishida",
    "Okina Matara", "Eika Ebisu", "Urumi Ushizaki", "Kutaka Niwatari", "Yachie Kicchou", "Mayumi Joutouguu",
    "Keiki Haniyasushin", "Saki Kurokoma", "Yuuma Toutetsu", "Mike Goutokuji", "Takane Yamashiro",
    "Sannyo Komakusa", "Misumaru Tamatsukuri", "Tsukasa Kudamaki", "Megumu Iizunamaru", "Chimata Tenkyuu",
    "Momoyo Himemushi", "Son Biten", "Enoko Mitsugashira", "Chiyari Tenkajin", "Hisami Yomotsu", "Zanmu Nippaku",

    # --- Literature, Manga and Music CDs ---
    "Hieda no Akyuu", "Tokiko", "Watatsuki no Toyohime", "Watatsuki no Yorihime", "Reisen (Lunar Rabbit)",
    "Sunny Milk", "Luna Child", "Star Sapphire", "Kasen Ibaraki", "Kosuzu Motoori", "Miyoi Okunoda",
    "Mizuchi Miyadeguchi", "Renko Usami", "Maribel Hearn", "Rin Satsuki (Scrapped)", "Layla Prismriver"
],
    "Danganronpa" : all_danganronpa_girls,
    "Persona" : [
    # Persona 1 (Revelations: Persona)
    "Maki Sonomura", "Eriko Kirishima", "Yuka Ayase", "Saeko Takami", "Reiji Kido (Mother)", 
    
    # Persona 2: Innocent Sin / Eternal Punishment
    "Maya Amano", "Lisa Silverman", "Ulala Serizawa", "Eriko Kirishima", "Yukino Mayuzumi",
    "Junko Kurosu", "Anna Yoshizaka", "Maki Sonomura",
    
    # Persona 3 / FES / Portable / Reload
    "Mitsuru Kirijo", "Yukari Takeba", "Fuuka Yamagishi", "Aigis", "Elizabeth", 
    "Chihiro Fushimi", "Yukari Takeba", "Rio Iwasaki", "Saori Hasegawa", "Kotone Shiomi", 
    "Chidori Yoshino", "Natsuki Moriyama", "Toriumi Isako", "Maya (P3)", "Metis",
    
    # Persona 4 / Golden
    "Chie Satonaka", "Yukiko Amagi", "Rise Kujikawa", "Naoto Shirogane", "Nanako Dojima", 
    "Margaret", "Marie", "Sayoko Uehara", "Ai Ebihara", "Eri Minami", "Hisano Kuroda", 
    "Mayumi Yamano", "Saki Konishi", "Noriko Kashiwagi", "Hanako Ohtani",
    
    # Persona 5 / Royal / Strikers
    "Ann Takamaki", "Makoto Niijima", "Futaba Sakura", "Haru Okumura", "Kasumi Yoshizawa", 
    "Sumire Yoshizawa", "Morgana (Female form/theory - strictly human appearance)", 
    "Sae Niijima", "Sadayo Kawakami", "Tae Takemi", "Ichiko Ohya", "Chihaya Mifune", 
    "Hifumi Togo", "Lavenza", "Caroline", "Justine", "Wakaba Isshiki", "Shiho Suzui", 
    "Sophia", "Zenzei Akane", "Alice Hiiragi", "Erine", "Toshiro's Mother",

    # Velvet Room / Spin-offs / Antagonists
    "Belladonna", "Tatsuya's Mother", "Yumi Ozawa", "Ayane Matsunaga", "Rei", "Hikari"
],
    "Fate" : [
    # Fate/stay night & Fate/hollow ataraxia
    "Artoria Pendragon (Saber)", "Rin Tohsaka", "Sakura Matou", "Illyasviel von Einzbern", 
    "Medea (Caster)", "Medusa (Rider)", "Taiga Fujimura", "Ayako Mitsuzuri", "Sella", "Leysritt", 
    "Stheno", "Euryale", "Bazett Fraga McRemitz", "Caren Hortensia", "Justeaze Lizrich von Einzbern",

    # Fate/Zero
    "Irisviel von Einzbern", "Maiya Hisau", "Aoi Tohsaka", "Sola-Ui Nuada-Re Sophia-Ri", 
    "Natalia Kaminski", "Shirley",

    # Fate/Extra & Fate/Extra CCC
    "Nero Claudius", "Tamamo-no-Mae", "Francis Drake", "Alice", "Nursery Rhyme", 
    "Rani VIII", "Misao Amari", "Hakuno Kishinami (Female)", "BB", "Meltryllis", 
    "Passionlip", "Kingprotea", "Violet", "Kazuradrop", "Suzuka Gozen", "Sessyoin Kiara",

    # Fate/Apocrypha
    "Jeanne d'Arc (Ruler)", "Mordred", "Atalanta", "Semiramis", "Frankenstein", 
    "Jack the Ripper", "Fiore Forvedge Yggdmillennia", "Celenike Icecolle Yggdmillennia", 
    "Reika Rikudou", "Laeticia",

    # Fate/Grand Order (Servants & NPCs)
    "Mash Kyrielight", "Olga Marie Animusphere", "Da Vinci (Rider/Caster)", "Altera", 
    "Scathach", "Boudica", "Ushiwakamaru", "Marie Antoinette", "Martha", "Mata Hari", 
    "Carmilla", "Elizabeth Bathory", "Kiyohime", "Jing Ke", "Okita Souji", "Oda Nobunaga", 
    "Miyamoto Musashi", "Nitocris", "Ishtar", "Ereshkigal", "Quetzalcoatl", "Gorgon", 
    "Tiamat", "Scheherazade", "Penthesilea", "Kato Danzo", "Queen Medb", "Circe", 
    "Osakabehime", "Nezha", "Abigail Williams", "Katsushika Hokusai", "Semiramis", 
    "Anastasia Nikolaevna Romanova", "Atalanta Alter", "Valkyrie (Ortlinde, Hildr, Thrud)", 
    "Sitonai", "Yu Mei-ren", "Bradamante", "Beni-enma", "Murasaki Shikibu", "Kama", 
    "Lakshmibai", "Nagao Kagetora", "Charlotte Corday", "Europa", "Sei Shonagon", 
    "Caenis", "Pollux", "Kijyo Koyo", "Artoria Caster", "Himiko", "Van Gogh", "Ibuki Douji", 
    "Vritra", "Taira no Kagekiyo", "Kiichi Hogen", "Galatea", "Morgan le Fay", 
    "Baobhan Sith", "Barghest", "Melusine", "Koyanskaya of Light", "Koyanskaya of Darkness", 
    "Jacques de Molay", "Zenobia", "Dobrynya Nikitich", "Hephaestion", "Trung Sisters", 
    "Krimhild", "Utsumi Erice", "Lady Avalon", "Xu Fu", "Archetype: Earth (Arcueid)", 
    "Sen-no-Rikyu", "Kukulkan", "Tiangong", "Duryodhana (Female version)", "Sodoma's Beast",

    # Fate/strange fake & others
    "Ayaka Sajyou", "Tine Chelc", "Francesca Prelati", "Hassan of Intoxicated Dream", 
    "Manaka Sajyou", "Misaya Reiroukan", "Gray", "Reines El-Melloi Archisorte", "Luvia Edelfelt"
],
    "Zenless Zone Zero": [
    # Cunning Hares 
    "Anby Demara", 
    "Nicole Demara", 
    "Nekomiya Mana (Nekomata)", 
    
    # Belobog Heavy Industries 
    "Koleda Belobog", 
    "Grace Howard", 
    
    # Victoria Housekeeping Co. 
    "Ellen Joe", 
    "Alexandrina Sebastiane (Rina)", 
    "Corin Wickes", 
    
    # Section 6 
    "Hoshimi Miyabi", 
    "Soukaku", 
    "Tsukishiro Yanagi", 
    
    # Criminal Investigation 
    "Zhu Yuan", 
    "Qingyi", 
    "Jane Doe", 
    
    # Sons of Calydon 
    "Luciana de Montefio (Lucy)", 
    "Piper Wheel", 
    "Caesar King", 
    "Burnice White",
    
    # Obol Squad 
    "Soldier 11",
    "Trigger",
    "Orphie",
    "Seed (Flora)",
    
    "Evelyn Chevalier",  # Stars of Lyra
    "Astra Yao",         # Stars of Lyra
    "Aria",              # Angels of Delusion
    "Sunna",             # Angels of Delusion
    "Cissia",            # Новое в 2.7
    "Nangong Yu",        # Новое в 2.7
    "Ye Shunguang",      # Yunkui Summit
    "Ju Fufu",           # Yunkui Summit
    "Yixuan",            # Yunkui Summit
    "Yidhari Murphy",    # Spook Shack
    "Lucia Elowen",      # Spook Shack
    "Alice Thymefield",  # Spook Shack
    "Yuzuha",            # Spook Shack
    "Banyue",
    "Dialyn",
    "Pulchra Fellini",
    "Vivian",
    "Zhao",
    
    # Protagonist
    "Belle"
],
    "Umamusume": [
    "Special Week", "Silence Suzuka", "Tokai Teio", "Maruzensky", "Fuji Kiseki", 
    "Oguri Cap", "Gold Ship", "Vodka", "Daiwa Scarlet", "Taiki Shuttle", 
    "Grass Wonder", "Hishi Amazon", "Mejiro McQueen", "El Condor Pasa", "細江純子 (Hosoe Junko)",
    "T.M. Opera O", "Narita Brian", "Symboli Rudolf", "Air Groove", "Agnes Digital", 
    "Seiun Sky", "Tamamo Cross", "Fine Motion", "Biwa Hayahide", "Mayano Top Gun", 
    "Manhattan Cafe", "Mihono Bourbon", "Mejiro Ryan", "Hishi Akebono", "Yukino Bijin", 
    "Rice Shower", "Inez Fujin", "Agnes Tachyon", "Admire Vega", "Inari One", 
    "Winning Ticket", "Air Shakur", "Eishin Flash", "Curren Chan", "Kawakami Princess", 
    "Golden City", "Sakura Bakushin O", "Seeking the Pearl", "Shinko Windy", "Sweep Tosho", 
    "Super Creek", "Smart Falcon", "Zenno Rob Roy", "Tosen Jordan", "Nakayama Festa", 
    "Narita Taishin", "Nishino Flower", "Haru Urara", "Bamboo Memory", "Biko Pegasus", 
    "Marvelous Sunday", "Matikanefukutaru", "Mr. C.B.", "Meisho Doto", "Mejiro Dober", 
    "Nice Nature", "King Halo", "Machiikane Tannhauser", "Ikuno Dictus", "Turumumi Zenno",
    "Mejiro Palmer", "Daitaku Helios", "Twin Turbo", "Satono Diamond", "Kitasan Black", 
    "Sakura Chiyono O", "Sirius Symboli", "Mejiro Ardan", "Yaeno Muteki", "Tsurumaru Tsuyoshi", 
    "Mejiro Bright", "Sakura Laurel", "Narita Top Road", "Yamanin Zephyr", "Aston Machan", 
    "Satono Crown", "シュヴァルグラン (Cheval Grand)", "ケイエスミラクル (K.S. Miracle)",
    "Jungle Pocket", "Katsuragi Ace", "Neo Universe", "Hishi Miracle", "Tap Dance City",
    "Duramente", "Line Craft", "Cesario", "Air Messiah", "Dare Dare Dare",
    "Gentildonna", "Orfevre", "Win Variation", "Still in Love", "No Reason"
],
    "Blue Archive": [
    "Airi", "Akane", "Akari", "Ako", "Aris", "Ami", "Aona", "Aoi", "Arona", "Aru", 
    "Asuna", "Atsuko", "Ayane", "Azusa", "Cherino", "Chihiro", "Chinatsu", "Chise", 
    "Eimi", "Eri", "Fubuki", "Fuuka", "Hanae", "Hanako", "Hare", "Haruka", "Haruna", 
    "Hasumi", "Hibiki", "Hifumi", "Hikari", "Himari", "Hina", "Hinata", "Hiyori", 
    "Hoshino", "Ibuki", "Ichika", "Iori", "Izumi", "Izuna", "Junko", "Juri", "Kaede", 
    "Kaho", "Kanna", "Karin", "Kasumi", "Kayoko", "Kazusa", "Kei", "Kikyou", "Kirara", 
    "Kirino", "Kisaki", "Koharu", "Kokona", "Konoka", "Kotama", "Kotori", "Koyuki", 
    "Maki", "Makoto", "Mari", "Marina", "Mashiro", "Megu", "Meru", "Michiru", 
    "Midori", "Mika", "Mimori", "Mina", "Mine", "Minori", "Misaki", "Miyako", 
    "Miyu", "Miyo", "Moe", "Momoi", "Momoji", "Mutsuki", "Nagisa", "Nagusa", "Natsu", 
    "Neru", "Niya", "Noa", "Nodoka", "Nonomi", "Nozomi", "Pina", "Rabu", "Rei", 
    "Reijo", "Reisa", "Renge", "Rio", "Ritsu", "Rumi", "Saki", "Sakurako", "Saori", 
    "Saten Ruiko", "Saya", "Seia", "Sena", "Serika", "Serina", "Shigure", "Shimiko", 
    "Shiroko", "Shiroko Terror", "Shizuko", "Shun", "Subaru", "Sumire", "Suzumi", 
    "Takane", "Toki", "Tomoe", "Tsubaki", "Tsukuyo", "Tsurugi", "Ui", "Umika", 
    "Utaha", "Wakamo", "Yoshimi", "Yuuka", "Yuzu"
], 
    "Genshin Impact": [
    "Aino", "Aloy", "Amber", "Arlecchino", "Barbara", "Beidou", "Candace", 
    "Charlotte", "Chasca", "Chevreuse", "Chiroi", "Citlali", "Clorinde", 
    "Collei", "Columbina", "Dehya", "Diona", "Dori", "Emilie", "Eula", 
    "Faruzan", "Fischl", "Furina", "Ganyu", "Hu Tao", "Iansan", "Jahoda", 
    "Jean", "Kachina", "Keqing", "Kirara", "Klee", "Kuki Shinobu", "Kujou Sara", 
    "Lan Yan", "Lauma", "Layla", "Lisa", "Lumine", "Lynette", "Mavuika", 
    "Mona", "Mualani", "Nahida", "Navia", "Nilou", "Ningguang", "Noelle", 
    "Qiqi", "Raiden Shogun", "Rosaria", "Sangonomiya Kokomi", "Sayu", "Shenhe", 
    "Sigewinne", "Skirk", "Sucrose", "Varesa", "Xiangling", "Xianyun", 
    "Xilonen", "Xinyan", "Yae Miko", "Yanfei", "Yaoyao", "Yelan", "Yoimiya", 
    "Yun Jin"
],
    "Hololive": [
    # hololive JP
    "Tokino Sora", "Roboco-san", "AZKi", "Sakura Miko", "Hoshimachi Suisei",
    "Aki Rosenthal", "Shirakami Fubuki", "Natsuiro Matsuri", "Akai Haato", "Yozora Mel",
    "Minato Aqua", "Murasaki Shion", "Nakiri Ayame", "Yuzuki Choco", "Oozora Subaru",
    "Ookami Mio", "Nekomata Okayu", "Inugami Korone",
    "Usada Pekora", "Shiranui Flare", "Shirogane Noel", "Houshou Marine", "Uruha Rushia",
    "Amane Kanata", "Tsunomaki Watame", "Tokoyami Towa", "Himemori Luna", "Kiryu Coco",
    "Yukihana Lamy", "Momosuzu Nene", "Shishiro Botan", "Omaru Polka", "Mano Aloe",
    "La+ Darknesss", "Takane Lui", "Hakui Koyori", "Kazama Iroha", "Sakamata Chloe",
    
    # DEV_IS (ReGLOSS & FLOW GLOW)
    "Hiodoshi Ao", "Otonose Kanade", "Ichijou Ririka", "Juufuutei Raden", "Todoroki Hajime",
    "Isaki Riona", "Koganei Niko", "Mizumiya Su", "Rindo Chihaya", "Kikirara Vivi",

    # hololive English
    "Mori Calliope", "Takanashi Kiara", "Ninomae Ina'nis", "Gawr Gura", "Watson Amelia",
    "IRyS", "Sana Tsukumo", "Ceres Fauna", "Ouro Kronii", "Nanashi Mumei", "Hakon Taro",
    "Shiori Novella", "Koseki Bijou", "Nerissa Ravencroft", "Fuwawa Abyssgard", "Mococo Abyssgard",
    "Elizabeth Rose Bloodflame", "Gigi Murin", "Cecilia Immergreen", "Raora Panthera",

    # hololive Indonesia
    "Ayunda Risu", "Moona Hoshinova", "Airani Iofifteen",
    "Kureiji Ollie", "Anya Melfissa", "Pavolia Reine",
    "Vestia Zeta", "Kaela Kovalskia", "Kobo Kanaeru",

    # hololive China (Historical)
    "Yogiri", "Civia", "Spade Echo", "Doris", "Artia", "Rosalyn"
],
    "Honkai: Star Rail": [
    "Acheron","Aglaea","Asta","Bailu","Black Swan","Bronya","Castorice","Cerydra","Cipher","Clara",
    "Cyrene","The Dahlia","Evernight","Feixiao","Firefly","Fu Xuan","Fugue","Guinaifen","Hanya",
    "Herta","The Herta","Himeko","Hook","Huohuo","Hyacine","Hysilens","Jade",
    "Jingliu","Kafka","Lingsha","Lynx","March 7th","Natasha","Pela","Qingque","Rappa","Robin","Ruan Mei",
    "Seele","Serval","Silver Wolf","Sparkle","Sparxie","Stelle","Sushang","Tingyun","Topaz","Tribbie","Xueyi","Yao Guang","Yukong","Yunli"
],
    "Azure Lare": [
    "Abukuma", "Acasta", "Achilles", "Aconit", "Admiral Graf Spee", "Admiral Hipper", "Admiral Hipper (Muse)", 
    "Admiral Nakhimov", "Admiral Scheer", "Admiralty Region", "Aegir", "Agano", "Ajax", "Akagi", 
    "Akagi (Muse)", "Akagi-chan", "Akashi", "Akatsuki", "Akizuki", "Alabama", "Albacore", "Alberico da Barbiano", 
    "Albrecht von Roon", "Alcedo", "Aldea", "Algerie", "Algerie META", "Allen M. Sumner", "Alsace", 
    "Alvitr", "Amagi", "Amagi-chan", "Amazon", "Ambush", "Amethyst", "An Shan", "Anchorage", "Andrea Doria", 
    "Antonin", "Aoba", "Aquila", "Arashio", "Ardent", "Arethusa", "Argus", "Ariake", "Arizona", "Arizona META", 
    "Ark Royal", "Ark Royal META", "Arkhangelsk", "Armstrong", "Asagumo", "Asashio", "Ashigara", "Astoria", 
    "Atago", "Atlanta", "Attilio Regolo", "August von Parseval", "Aurora", "Avrora", "Ayanami", "Aylwin", 
    "Azuma", "Bache", "Bacu", "Badger", "Bainbridge", "Baltimore", "Baltimore (Muse)", "Bancroft", "Barb", 
    "Barham", "Bartolomeo Colleoni", "Bataan", "Bayeux", "Béarn", "Béarn META", "Beagle", "Beeler", "Belfast", 
    "Bellona", "Belorussiya", "Benoit", "Bennington", "Benson", "Bergamini", "Berwick", "Biloxi", "Billings", 
    "Birmingham", "Bismarck", "Bismarck Zwei", "Black Prince", "Blücher", "Boadicea", "Boise", "Bolzano", 
    "Bon Homme Richard", "Bordeaux", "Borden", "Borie", "Boscawen", "Bremerton", "Brest", "Bretagne", 
    "Bristol", "Brooklyn", "Brünhilde", "Bulldog", "Bunker Hill", "Bush", "California", "Callen", "Cambeltown", 
    "Canberra", "Carabiniere", "Card", "Carysfort", "Cassin", "Cassard", "Castore", "Cavour", "Centaur", 
    "Chao Ho", "Chang Chun", "Chapayev", "Charles Ausburne", "Chaser", "Charybdis", "Chen Hai", "Cheshire", 
    "Chevalier Paul", "Chicago", "Chikuma", "Chikuma II", "Chitose", "Chiyoda", "Choukai", "Chung King", 
    "Cilliers", "Clémenceau", "Cleveland", "Cleveland (Muse)", "Coley", "Colorado", "Columbia", "Columbus", 
    "Comte de Grasse", "Concord", "Condé", "Constellation", "Conte di Cavour", "Cooper", "Copernicus", 
    "Coral Sea", "Cornwall", "Cossack", "Courageous", "Courbet", "Crescent", "Cromwell", "Cumberland", 
    "Curacoa", "Curlew", "Cygnet", "Dace", "Daihou", "Daihou (Muse)", "Daihou-chan", "Dakota", "Dandolo", 
    "Danton", "Daring", "Dauntless", "D'Eon", "De Grasse", "Defender", "Delaware", "Dentsu", "Denver", 
    "Derfflinger", "Des Moines", "Detroit", "Dewey", "Dido", "Dido (Muse)", "Doris", "Dorsetshire", "Downes", 
    "Dragon", "Drake", "Dreadnought", "Dupleix", "Duras", "Dvenadtsat Apostolov", "Eagle", "Echo", "Eckernförde", 
    "Ecton", "Edinburgh", "Eisenzahn", "Eldridge", "Eldridge META", "Elisabeth", "Elbe", "Emanuele Pessagno", 
    "Emden", "Emile Bertin", "Enterprise", "Enterprise META", "Erebus", "Eskimo", "Essex", "Eugen", 
    "Euryalus", "Exeter", "Exmouth", "Foch", "Fletcher", "Flint", "Florence", "Florida", "Foch", "Foch META", 
    "Forbin", "Forbin META", "Formidable", "Formidable (Muse)", "Forrest", "Fortune", "Fortune META", 
    "Foxhound", "Franklin", "Friedrich der Große", "Fubuki", "Fuji", "Fumizuki", "Furutaka", "Fusou", 
    "Fusou META", "Galatea", "Gali", "Gambia", "Gangut", "Gascogne", "Gascogne (Muse)", "Gascogne-chan", 
    "Gascoyne", "Gemsbok", "Gentry", "Geoffroy", "George V", "Georgia", "German", "Giuseppe Garibaldi", 
    "Glowworm", "Gloucester", "Gneisenau", "Gneisenau META", "Gorgon", "Gorky", "Gotland", "Graf Zeppelin", 
    "Grenville", "Gromkiy", "Grothe", "Grozny", "Guam", "Guichen", "Guinevere", "Gwin", "Haguro", "Hai Chi", 
    "Hai Tien", "Hakuryuu", "Halford", "Hall", "Halle", "Hamakaze", "Hammann", "Hammann II", "Hanazuki", 
    "Hancock", "Harbin", "Hardy", "Haruna", "Haruna META", "Harusame", "Hatsuharu", "Hatsushimo", "Hatsuzuki", 
    "Hau", "Havock", "Hawkins", "Hayasui", "Hayate", "Hazelwood", "Hebe", "Heermann", "Heisenberg", "Heishin", 
    "Helena", "Helena META", "Helena II", "Hermes", "Hermione", "Hestia", "Hibiki", "Hiei", "Hiei-chan", 
    "Hindenburg", "Hipper", "Hiryuu", "Hiryuu META", "Hiyou", "Hiyou META", "Hobby", "Holloway", "Homewood", 
    "Honolulu", "Hood", "Hornet", "Hornet II", "Hotspur", "Houston", "Houston II", "Howe", "Hua Mei", 
    "Huan Ch'ang", "Hugenot", "Hughes", "Hume", "Hunter", "Hunter META", "Huron", "Hyuga", "Hyuga META", 
    "I-13", "I-168", "I-19", "I-25", "I-26", "I-56", "I-58", "Ibuki", "Icarus", "Ikazuchi", "Illustrious", 
    "Illustrious (Muse)", "Illustrious-chan", "Impero", "Implacable", "Inazuma", "Independence", "Indomitable", 
    "Indomitable (Muse)", "Indianapolis", "Indy", "Ingraham", "Intrepid", "Ise", "Ise META", "Isuzu", 
    "Isokaze", "Italia", "Izumo", "Jaff", "Jahn", "Janus", "Jarvis", "Javelin", "Jean Bart", "Jean Bart META", 
    "Jeanne d'Arc", "Jenkins", "Jervis", "Johnston", "Juneau", "Juneau META", "Juno", "Jupiter", "Jura", 
    "Kaga", "Kaga (Muse)", "Kagerou", "Kako", "Kala", "Kalinin", "Kamikaze", "Karlsruhe", "Kars", "Kashino", 
    "Kasumi", "Kasumi-chan", "Kawakaze", "Kearsarge", "Keelung", "Kelly", "Kent", "Kersaint", "Kidd", "Kiev", 
    "Kikuzuki", "King George V", "Kinu", "Kinugasa", "Kirishima", "Kirishima META", "Kirov", "Kitakaze", 
    "Kiyonami", "KMS Admiral Hipper", "KMS Bismarck", "KMS Friedrich der Grosse", "KMS Graf Zeppelin", 
    "KMS Prinz Eugen", "KMS Roon", "KMS Tirpitz", "KMS Zeppelin", "Kobe", "Königsberg", "Köln", "Kongou", 
    "Kongou II", "Konigsberg", "Krasny Krym", "Kronshtadt", "Kumano", "Kursk", "Kutuzov", "Kuwana", "Kyzyl", 
    "La Galissonnière", "La Galissonnière META", "Laffey", "Laffey II", "Langley", "Langley II", "Lansdowne", 
    "Laplace", "L'Audacieux", "L'Indomptable", "Le Malin", "Le Malin (Muse)", "Le Mars", "Le Mars META", 
    "Le Terrible", "Le Triomphant", "Leander", "Lecce", "Lee", "Leipzig", "Lena", "Leonardo da Vinci", 
    "L'Opiniâtre", "Lexington", "Libre", "L'Inconstant", "Li'l Sandy", "Lince", "Lincoln", "Lindemann", 
    "L'Indomptable", "Little Bel", "Little Cheshire", "Little Enterprise", "Little Formidable", 
    "Little Illustrious", "Little Renown", "Little San Diego", "Little Spee", "Littorio", "Liverpool", 
    "London", "Long Island", "Lookout", "L'Opiniâtre", "Lorraine", "L'Ouverture", "Lovelace", "Lowe", 
    "Luce", "Ludlow", "Lützow", "Lumiere", "L'Unité", "Luxembourg", "Lyon", "Maury", "Marseillaise", 
    "Mackensen", "Maddeley", "Magdeburg", "Mainz", "Makarov", "Makinami", "Malaya", "Manchester", "Manly", 
    "Marco Polo", "Marseillaise", "Maryland", "Massachusetts", "Matsu", "Matsukaze", "Maya", "Maury", 
    "Mazzo", "Mec", "Medis", "Meitetsu", "Memphis", "Memphis META", "Meyrant", "Michishio", "Middlesex", 
    "Mikasa", "Mikazuki", "Milton", "Minagawa", "Minami", "Minneapolis", "Minotaur", "Mint", "Mogador", 
    "Mogami", "Monarch", "Monmouth", "Montpelier", "Moreno", "Morrill", "Mouve", "Murasame", "Murmansk", 
    "Musashi", "Mutsu", "Mutsu META", "Mutsuki", "Myoukou", "Nachi", "Naganami", "Nagato", "Nagato META", 
    "Nagato-chan", "Nakano", "Namiki", "Napoli", "Nara", "Narvik", "Nashville", "Nassau", "Natsushio", 
    "Neptune", "Nevada", "New Jersey", "New Orleans", "Newcastle", "Nicholas", "Nieuw Amsterdam", "Nikolay", 
    "Ning Hai", "Niobe", "Niizuki", "Noshiro", "Nosher", "North Carolina", "Northampton", "Northampton II", 
    "Nosher", "Nowaki", "Nurnberg", "Oakland", "Oatley", "Oboro", "Oceanic", "Odin", "Oite", "Okie", 
    "Oklahoma", "Oldendorf", "Omaha", "Onslow", "Orel", "Orestes", "Orion", "Orizaba", "Orleans", "Orpheus", 
    "Osiris", "Ostrovsky", "Otsu", "Oushio", "Owari", "Oxford", "Pamiat Merkuria", "Pamiat Merkuria META", 
    "Pansy", "Paris", "Parsons", "Pas-de-Calais", "Pathfinder", "Patriot", "Pauillac", "Paul", "Pellegrini", 
    "Pelly", "Penelope", "Pennsylvania", "Pensacola", "Perceval", "Perseus", "Peter Strasser", "Petropavlovsk", 
    "Phoenix", "Pickering", "Ping Hai", "Pionier", "Pioneer", "Piotr Velikiy", "Pleiades", "Plymouth", 
    "Pola", "Pommern", "Portland", "Porthos", "Potemkin", "Pratt", "Preston", "Primauguet", "Prince of Wales", 
    "Princess Royal", "Prinz Adalbert", "Prinz Eugen", "Prinz Heinrich", "Prinz Rupprecht", "Provence", 
    "Pueblo", "Purifier", "Pyotr Velikiy", "Quaker", "Queen Elizabeth", "Queen Elizabeth META", 
    "Queen Mary", "Quincy", "Radford", "Raleigh", "Ramsay", "Ran", "Ranger", "Ranier", "Rapide", "Rasnoye", 
    "Rathenow", "Raty", "Raven", "Ray", "Recif", "Regensburg", "Regulus", "Reid", "Remedios", "Renown", 
    "Renown META", "Repulse", "Repulse META", "Resolution", "Revenge", "Richmond", "Richelieu", "Rion", 
    "River", "Rivière", "Rodney", "Rodney META", "Roe", "Roma", "Rooks", "Roon", "Roon (Muse)", "Rossiya", 
    "Rostov", "Royal Oak", "Royal Sovereign", "Rupprecht", "Ryuuhou", "Ryujo", "Ryujo META", "S-1", "S-2", 
    "S-3", "S-4", "S-5", "S-10", "Saint Louis", "Saipan", "Sakai", "Sakawa", "Salem", "Salt Lake City", 
    "San Diego", "San Francisco", "San Jacinto", "San Martino", "Santa Cruz", "Santa Fe", "Saratoga", 
    "Scharnhorst", "Scharnhorst META", "Scherzo", "Schröder", "Scipione Africano", "Scylla", "Seattle", 
    "Sedan", "Sento", "Serafim", "Severn", "Seydlitz", "Sheffield", "Sheffield (Muse)", "Sheffield META", 
    "Shiba", "Shigure", "Shimakaze", "Shimanto", "Shinano", "Shinano-chan", "Shirakumo", "Shiratsuyu", 
    "Shirayuki", "Sho", "Shouhou", "Shoukaku", "Shropshire", "Simo", "Sims", "Siren", "Smaland", "Smalley", 
    "Smolensk", "Soobrazitelny", "South Carolina", "South Dakota", "Southampton", "Sovetskaya Belorussiya", 
    "Sovetskaya Rossiya", "Sovetsky Soyuz", "Speedy", "Spence", "Splendid", "St. Lawrence", "St. Louis", 
    "Stanly", "Stephen Potter", "Strasbourg", "Suffolk", "Suffren", "Sulin", "Sumner", "Sun Yat-sen", 
    "Surcouf", "Suruga", "Sussex", "Suzuya", "Svea", "Swiftsure", "Sydney", "Syren", "Syzran", "Tacoma", 
    "Taihou", "Taihou META", "Tainui", "Taishou", "Takahiro", "Takao", "Takao META", "Talahassee", 
    "Talento", "Tallinn", "Tanikaze", "Tarantini", "Tartu", "Tashkent", "Tashkent (Muse)", "Tatsuta", 
    "Tenryuu", "Terpsichore", "Terrible", "Terror", "Texas", "Thetis", "Thorn", "Thuringen", "Ticonderoga", 
    "Ting An", "Tirpitz", "Tobias", "Tone", "Topaz", "Torbay", "Torricelli", "Tosa", "Tourville", "Towada", 
    "Trento", "Trento META", "Trieste", "Trinidad", "Triton", "Triumph", "Tromp", "Tyne", "U-37", "U-47", 
    "U-73", "U-81", "U-96", "U-101", "U-110", "U-1206", "U-410", "U-522", "U-556", "U-556 META", "U-557", 
    "U-101", "U-47", "U-81", "U-96", "U-37", "Ulrich von Hutten", "Unicorn", "Uranie", "Urchin", "Urho", 
    "Urusei", "Ushio", "Utah", "U-557", "U-556", "U-81", "U-96", "V-1", "V-2", "V-3", "Valiant", "Vampire", 
    "Vampire META", "Vanguard", "Vauquelin", "Vengeance", "Vento", "Venus", "Verdun", "Verite", "Vestal", 
    "Vestal META", "Vichy", "Victoria", "Victorious", "Vidette", "Vincennes", "Vindex", "Viper", "Viribus Unitis", 
    "Vittorio Veneto", "Volga", "Voroshilov", "Vouquelin", "Vyborg", "Wakatake", "Wales", "Walker", "Wallis", 
    "Warspite", "Warspite META", "Washington", "Wasp", "Wasp II", "Watatsumi", "Weber", "Wedderburn", 
    "Wellington", "Wesel", "Weser", "West Virginia", "Whitehead", "Wichita", "Wilder", "Wilkes", "William D. Porter", 
    "Windsor", "Winnipeg", "Wisconsin", "Wittelsbach", "Wolfhound", "Worcester", "Wren", "Wuah", "Xenon", 
    "Xi An", "Xing An", "Yagami", "Yahagi", "Yakumo", "Yamashiro", "Yamashiro META", "Yamato", "Yat Sen", 
    "Yeon", "Yoizuki", "York", "Yorktown", "Yorktown II", "Yūachi", "Yūgure", "Yūnagagi", "Yūshio", 
    "Yukikaze", "Yura", "Z1", "Z2", "Z16", "Z18", "Z19", "Z20", "Z21", "Z23", "Z24", "Z25", "Z26", "Z28", 
    "Z35", "Z36", "Z43", "Z46", "Z47", "Zuihou", "Zuikaku"
]
}

title_list = list(girls_characters_dict.keys())