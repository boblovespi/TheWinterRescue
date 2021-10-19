import os

ftbquests_path = "config/ftbquests/quests/chapters"
zh_cn_path = "kubejs/assets/twr_quests/lang/zh_cn.json"
en_us_path = "kubejs/assets/twr_quests/lang/en_us.json"
should_replace_key = [
    "			title",
    "			subtitle"
]
context_dict = {}


def check_dir(path):
    for file in os.listdir(path):
        file_path = path + "/" + file
        if (os.path.isdir(file_path)):
            check_dir(file_path)
        else:
            read_snbt(file_path, file)


def read_snbt(full_path, file_name):
    f = open(full_path, "r+", encoding='utf-8')
    f_list = f.readlines()
    file_name = file_name.split(".snbt")[0]
    f.close()

    quests_list = []
    quests_start_index_list = []
    quest_start_line = 0
    quest_end_line = 0
    found_quest_start = False
    found_quest_end = False
    for i, line in enumerate(f_list):

        if found_quest_start and found_quest_end:
            quests_list.append(f_list[quest_start_line:quest_end_line+1])
            quests_start_index_list.append(quest_start_line)

        if line.startswith("		{"):
            quest_start_line = i
            found_quest_start = True

        if line.startswith("		}"):
            quest_end_line = i
            found_quest_end = True

    for k, quest in enumerate(quests_list):
        q_start_line_index = quests_start_index_list[k]
        quest_id = ""

        for m, find_id in enumerate(quest):
            if find_id.startswith("			id"):
                first_quote_index = find_id.find("\"")
                last_quote_index = find_id.rfind("\"")
                quest_id = find_id[first_quote_index + 1:last_quote_index]

        for n, quest_line in enumerate(quest):
            flag = False  # is true, then read quest text
            is_multiple_line = False
            j = 0
            if quest_line.startswith("			description"):
                flag = True
                if not quest_line.endswith("]"):
                    is_multiple_line = True
            if is_multiple_line and quest_line.startswith("			]"):
                flag = False
                is_multiple_line = False
                j = 0
            if flag:
                j += 1
                if is_multiple_line:
                    text_key = "description." + str(j)
                    replace_with_lang_key(quest_line, text_key, f_list, q_start_line_index + n, quest_id)
                    continue
                else:
                    flag = False
                    text_key = "description." + str(j)
                    replace_with_lang_key(quest_line, text_key, f_list, q_start_line_index + n, quest_id)
                    continue

            for key in should_replace_key:
                if quest_line.startswith(key):
                    replace_with_lang_key(quest_line, key.lstrip(), f_list, q_start_line_index + n, quest_id)

    f = open(full_path, "w+", encoding="utf-8")
    f.writelines(f_list)
    f.close()


def replace_with_lang_key(line, key, f_list, index, file_name):
    first_quote_index = line.find("\"")
    last_quote_index = line.rfind("\"")
    head = line[0:first_quote_index]
    content = line[first_quote_index + 1:last_quote_index]
    tail = line[last_quote_index + 1:len(line)]
    if not (content.startswith("{") and content.endswith("}")):
        lang_key = "quest.twr.%s.%s" % (file_name, key)
        print("get lang key %s, value = %s" % (lang_key, content))
        new_content = head + "\"{" + lang_key + "}\"" + tail
        f_list[index] = new_content
        context_dict[lang_key] = content.replace("\\", "")


def write_lang(path):
    copy = context_dict.copy()
    if (len(copy) == 0):
        return
    to_append_entries = []
    f = open(path, "r+", encoding='utf-8')
    f_list = f.readlines()
    f.close()
    f_list_copy = f_list.copy()
    for i, line in enumerate(f_list):
        if (line.startswith("#")):
            continue
        key = line.split("=")[0]
        if (key in copy):
            f_list_copy[i] = key + "=" + copy.pop(key) + "\n"
    for key, value in copy.items():
        to_append_entries.append(key + "=" + value)
    f = open(path, "w+", encoding="utf-8")
    f.writelines(f_list_copy)
    if (len(f_list[-1]) != 0 and f_list[-1] != "\n"):
        f.write("\n")
    for entry in to_append_entries:
        f.write(entry + "\n")
    f.close()


check_dir(ftbquests_path)
write_lang(zh_cn_path)
write_lang(en_us_path)
