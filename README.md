# flask-dep
Introduction
============

flask-dep is a interface designed to work with Apple's Device Enrollment Program (DEP) API. It is meant to be used as a means for 
Apple Resellers to be able to enroll their customers' eligible Apple devices into the customer institution's DEP account. Please consult the DEP API documentation ([UAT](https://applecareconnect.apple.com/api-docs/depuat/html/WSStart.html?user=reseller),
[Production](https://applecareconnect.apple.com/api-docs/dep/html/WSReference.html?user=reseller)) for more details.

This is being open-sourced to gather feedback on how to make the module better and benefit the community at large.

**Note**: Before an authorized reseller may begin enrolling devices for their customers, Apple must take both the reseller and the customer
through an onboarding process **AND** sign-off on the reseller's implementation of the DEP API. This is partially detailed in the 
[DEP Design Requirements](https://applecareconnect.apple.com/api-docs/depuat/html/WSImpManual.html?user=reseller&id=1111&lang=EN).
Please contact your Apple representative for more information.


Requirements
============

- Python 3.6 or later
- Contents of requirements.txt in your Python environment
- DEP client certs (UAT/PROD) signed by Apple