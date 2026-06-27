class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq = set()

        for email in emails:
            local, domain = email.split("@")

            if "+" in local:
                local = local.split("+")[0]

            name = local.replace(".", "")

            uniq.add(f"{name}@{domain}")

        return len(uniq)