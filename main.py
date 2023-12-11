import random
import streamlit as st


vowels = ["a", "e", "i", "o", "u"]
consonants = ["p", "t", "k", "s", "m", "n", "l", "w", "j"]


def get_vowel(previous_consonant: str) -> str:
    if previous_consonant.lower() in ["t", "j"]:
        vowel = random.choice([x for x in vowels if x != "i"])  # 母音は"i"以外
    elif previous_consonant.lower() == "w":
        vowel = random.choice([x for x in vowels if x not in ["o", "u"]])  # 母音は"o", "u"以外
    else:
        vowel = random.choice(vowels)
    return vowel


def get_head_letters() -> str:
    letters = ""
    random_num = random.random()
    if random_num < 0.3:
        letters += random.choice(vowels).upper()  # 母音から始まる
    else:
        letters += random.choice(consonants).upper()  # 子音から始まる
        letters += get_vowel(letters)
    return letters


def get_not_head_letters(previous_char: str) -> str:
    letters = ""
    if previous_char == "n":
        letters += random.choice([x for x in consonants if x not in ["m", "n"]])  # "m", "n"以外から始まる
        letters += get_vowel(letters)
    else:
        random_num = random.random()
        if random_num < 0.05:
            letters = "nja"
        elif random_num < 0.1:
            letters = "n"
        else:
            letters += random.choice(consonants)  # 子音から始まる
            letters += get_vowel(letters)
    return letters


def main():
    st.title("sina wile e nimi anu seme?")
    st.write("Setting \"nanpa kalama\" and pressing \"pali e nimi\" will generate a tokipona-like name.")

    num_sounds = st.slider("nanpa kalama", min_value=2, max_value=8, value=3)

    if st.button("pali e nimi"):
        name = get_head_letters()
        for _ in range(num_sounds - 1):
            name += get_not_head_letters(name[-1])
        st.header(f"nimi: {name}")


if __name__ == "__main__":
    main()