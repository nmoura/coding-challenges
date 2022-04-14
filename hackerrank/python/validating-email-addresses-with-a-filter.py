# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter
import re


def fun(s):
    regex = r'(\w|-)+@[a-z0-9]+\.[a-z]{1,3}$'
    return re.match(regex, s, re.ASCII)


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())


filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
