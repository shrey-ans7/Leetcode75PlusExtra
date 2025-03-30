class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        tracker=set()
        for email in emails:
            components=email.split("@")     
            localname=components[0]
            localname=localname.replace(".","") 
            localname=localname.split("+")[0] 
            domainname=components[1]
            tracker.add(localname+"@"+domainname) 
        return len(tracker)
