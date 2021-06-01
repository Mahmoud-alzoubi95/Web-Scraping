from web_scraper import *
def test_correct_count_of_citations():
    actual = get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')
    # print(actual)
    expected = 5
    assert actual == expected
def test_verify_that_preceding_passage():
    actual = get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico')
    expected = "During the three centuries of colonial rule, fewer than 700,000 Spaniards, most of them men, settled in Mexico.[citation needed] Europeans, Africans, and indigenous intermixed, creating a mixed-race casta population in a process known as mestizaje. Mestizos, people of mixed European-indigenous ancestry, constitute the majority of Mexico's population.\n"
    assert actual == expected

