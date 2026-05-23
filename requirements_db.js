const requirementsDB = {
    "Partnership Firm (AOP)": [
        "NTNs, Emails &amp; Registered Phone numbers of All Partners.",
        "Color copy of CNICs of Partners.",
        "Verified/signed Partnership Deed.",
        "Nomination &amp; Authorization of Principal Officer.",
        "Rent agreement / Ownership Documents of Business/Office Premises.",
        "Latest paid Electricity Bill of Business Premises.",
        "Business Letterhead."
    ],
    "Private Limited Company (Pvt Ltd)": [
        "SECP login details of Proposed Directors (if any).",
        "Three Proposed Names for the Company.",
        "Scanned CNICs, Phone, Email &amp; Profession of all Directors.",
        "Amount of Authorized and Paid-up Capital.",
        "Percentage of Subscription in Capital.",
        "Registered address of Proposed Company.",
        "Business Activity and Value Per Share.",
        "Name of the Chief Executive."
    ],
    "Single Member Company (SMC-Pvt Ltd)": [
        "SECP login details of the Proposed Director (if any).",
        "Three Proposed Names for the company.",
        "Scanned CNIC, Phone, Email &amp; Profession of Director.",
        "Amount of Authorized and Paid-up Capital.",
        "Registered address and Business Activity.",
        "Value Per Share."
    ],
    "Limited Liability Partnership (LLP)": [
        "Three Proposed Names.",
        "Details of LLP \u2013 Business Activity, Address &amp; Objectives.",
        "Details of Partners \u2013 CNIC, Phone Number, Email, Profession &amp; Shareholding.",
        "LLP Agreement.",
        "Rent Agreement / Ownership evidence of Business Premises.",
        "Utility Bill of the Business Premises."
    ],
    "Sales Tax / GST / STRN (FBR)": [
        "Bank Account Maintenance Certificate.",
        "Acquisition Date &amp; Business Activity details.",
        "GPS-tagged Photographs of the business premises.",
        "Color copy of CNICs of Partners/Directors.",
        "Rent agreement or ownership docs of Office premises.",
        "Latest paid electricity bill.",
        "Biometric Verification.",
        "Latest Balance Sheet.",
        "Consumer number with gas &amp; electricity supplier + utility meter pictures.",
        "Particulars of all branches (if any).",
        "Authorization of Principal Officer.",
        "GPS-tagged photographs of machinery (Manufacturer only).",
        "Post Verification visit (Manufacturer only)."
    ],
    "PRA \u2013 Punjab Revenue Authority": [
        "Color copy of CNICs (Front + Back).",
        "Phone Number, Email &amp; Business Letterhead.",
        "Utility Bill, Rent Agreement / Ownership evidence of Premises.",
        "Bank Account Maintenance Certificate.",
        "Acquisition Date &amp; Business Activity.",
        "Authority Letter.",
        "PRA Registration Application.",
        "Incorporation Certificate (for Pvt. Ltd Companies).",
        "MOA and AOA (for Pvt. Ltd Companies).",
        "Latest Form A &amp; 9 (for Pvt. Ltd Companies).",
        "Incorporation Certificate, MOA, AOA, Form A &amp; 29 (Company \u2014 detailed list).",
        "Rent agreement/ownership docs of Office premises.",
        "Letterhead &amp; Bank Account Certificate.",
        "Particulars of all branches (if any).",
        "Authorization of Principal Officer &amp; Signed Application Form."
    ],
    "IPO Trademark (TM) Registration": [
        "TM-1 Form in duplicate.",
        "Six representations affixed on a durable paper of 13\u00d78 inch.",
        "CNIC of the Trademark Holder / partners.",
        "Specification of goods or services sought to be protected in any class.",
        "Residential address of holder or Letterhead of the Business.",
        "Other Information or Documents as required."
    ],
    "IPO Copyrights Registration": [
        "Two Copies of work.",
        "Demand Draft / Pay order of fee as applicable per work.",
        "CNIC of the Copyrights Holder / partners.",
        "NOC from publisher if work has been published and publisher is different from applicant.",
        "Search certificate from Trademark Office if the work is capable of being used on goods.",
        "Residential address of holder or Letterhead of the Business.",
        "Power of attorney.",
        "Other Information or Documents as required."
    ],
    "IPO Patent Registration": [
        "Two Copies of work / invention description.",
        "Demand Draft / Pay order of applicable fee.",
        "CNIC of the Patent Holder / partners.",
        "Technical disclosure of the invention (claims, abstract, drawings).",
        "Residential address of holder or Letterhead of the Business.",
        "Power of attorney.",
        "Other Information or Documents as required during the process."
    ],
    "IPO Trademark Infringement Case": [
        "Application to Director Enforcement.",
        "IPO Registration Certificate.",
        "Original LOGO / Trademark.",
        "Fake Logo/Trademark (infringed copy).",
        "Any other document required during the process."
    ],
    "NGO / NPO / Society / Trust / Foundation": [
        "MOA and AOA of the Organization.",
        "Authorization of President / Chairman.",
        "Color copy of CNICs of all Members.",
        "NADRA Biometric Verification of all Members.",
        "Police Character Certificates of all Members.",
        "Rent agreement / Ownership docs of Organization office.",
        "Letterhead &amp; latest paid electricity bill.",
        "Phone Number and Email address of all members.",
        "Phone number and email address of organization.",
        "All Documents as required during the process."
    ],
    "Lahore Chamber of Commerce &amp; Industries (LCCI)": [
        "Application for grant of new membership (Business Letterhead).",
        "Completely filled in membership form, duly proposed and seconded by two valid members.",
        "CNICs of Proprietor / Partners / Directors.",
        "NTN Certificate of Sole Proprietor.",
        "NTN Certificate of Company/Firm along with NTN Certificates of Directors/Partners.",
        "Sales-Tax Registration certificate (if applicable).",
        "Utility Bill of Business Premises.",
        "FORM-C in case AOP.",
        "MOA, AOA, Form 9 and Incorporation Certificate (for Private Limited Company).",
        "Respective Business Bank Account Maintenance Certificate.",
        "Authority letter (Business Letterhead)."
    ],
    "PSEB \u2013 Pakistan Software Export Board": [
        "Company / Business NTN issued by FBR.",
        "CNIC of all Directors / Partners / Proprietor.",
        "Attested copy of MOA, AOA, Form-A, 29 and Incorporation Certificate (Companies only).",
        "Attested copy of Form-C and Partnership deed (for Partnership firms).",
        "Business Bank Statement of last six months or Bank Account Maintenance Letter/Certificate.",
        "Comprehensive Business Profile (including Name, Designation, Number of Managerial Staff)."
    ],
    "P@SHA \u2013 Pakistan IT Industry Association": [
        "Membership Category selection.",
        "CNIC, Name &amp; Email of CEO and HR Head.",
        "CNIC, Name &amp; Email of Person in Charge (if CEO is not available).",
        "Company Profile (including Address, Email, Phone number etc.).",
        "NTN and STRN Certificate, Form-C of Company.",
        "Last 3 Online Submitted Income Tax Returns or Projected Domestic &amp; Export Revenue.",
        "Name &amp; Phone Number of Proposer and Seconder Company (current P@sha Member).",
        "Details of Key Services/Products and their URLs.",
        "Country of Business (i.e. China, UAE etc.).",
        "Major Client Names."
    ],
    "PPRA \u2013 Public Procurement Regulatory Authority": [
        "Open PPRA (EPADS) website with CNIC, User &amp; Business name, Mobile no, valid Email and Password.",
        "NTN Inquiry from FBR.",
        "Active Status Income &amp; Sales Tax.",
        "Yearly Income Tax Return.",
        "Taxpayer Registration Certificate."
    ],
    "PSW \u2013 Pakistan Single Window": [
        "NTN of Firm/Business.",
        "CNIC: Principal Officer / Sole Proprietor.",
        "Mobile No. (As per FBR records).",
        "Biometric verification Slip (FBR\u2013PSW).",
        "Bank Maintenance Certificate.",
        "Email &amp; Mobile No. (used for bank account registration).",
        "Authority Letter."
    ],
    "SECP Company Easy Exit (Dissolution)": [
        "Board Resolution regarding Dissolution of company (Printed on Company Letterhead and signed by all members).",
        "Affidavit by CEO that No outstanding legal, financial, and statutory obligations on part of the company (Duly printed on Stamp paper and signed by CEO).",
        "Board Resolution regarding closure of Company's Official Bank Account (Printed on Company Letterhead and signed by all members).",
        "Auditor's Certificate."
    ],
    "Corporate Matters &amp; Litigation Services": [
        "Income Tax matters (Audits, Replies to Notices of Tax Assessment / Recovery / Penalties, Appeals).",
        "Sales Tax matters (Audits, Replies to Notices of Tax Assessment / Recovery / Penalties, Appeals).",
        "Professional Tax matters (Certifications, Replies to Notices of Tax Assessment / Recovery / Penalties).",
        "Corporate Tax Disputes (i.e. Withholding Tax etc.).",
        "Customs and Excise Matters.",
        "Property Tax (Replies to Notices of Recovery / Penalties etc.).",
        "Tax Fraud and Evasion Cases.",
        "Tax Recovery and Enforcement.",
        "Miscellaneous Tax-Related &amp; Other Litigations."
    ]
};