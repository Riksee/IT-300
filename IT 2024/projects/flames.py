def remove_match_char(l1, l2):
    for x in range(len(l1)):
        for y in range(len(l2)):

            if l1[x] == l2[y]:
                c = l1[x]

                l1.remove(c)
                l2.remove(c)

                l3 = l1 + ["*"] + l2
                return [l3, True]
            
    l3 = l1 + ["*"] + l2
    return[l3, False]

if __name__ == "__main__":
    n1 = input("Enter first name: ")
    n1 = n1.lower()
    n1.replace(" ", "")
    n1_list = list(n1)

    n2 = input("Enter second name: ")
    n2 = n2.lower()
    n2.replace(" ", "")
    n2_list = list(n2)

    proceed = True

    while proceed:
        ret_list = remove_match_char(n1_list, n2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")

        n1_list = con_list[: star_index]
        n2_list = con_list[star_index + 1:]

count = len(n1_list) + len(n2_list)

result = ["Friends", "Lovers", "Affection", " Marriage", "Enemies", "Siblings"]

while len(result) > 1:
    split_index = (count % len(result) - 1)

    if split_index >= 0:
        right = result[split_index + 1:]
        left = result[: split_index]

        result = right + left

    else:
        result = result[: len(result) - 1]

print("Relationship status :", result[0])

