const lawsDB = {
    "Taxation Laws": [
        { "title": "Income Tax Ordinance, 2001", "features": ["Heads of Income", "Self-Assessment", "Amended 2024"], "dataKey": "it_2001_text" },
        { "title": "Sales Tax Act, 1990", "features": ["VAT Principle", "Input Credit", "Registration"], "dataKey": "st_1990_text" },
        { "title": "Federal Excise Act, 2005", "features": ["Excise Duty", "Goods/Services"], "dataKey": "fe_2005_text" },
        { "title": "Customs Act, 1969", "features": ["Import/Export", "Duties"], "dataKey": "cu_1969_text" },
        { "title": "Benami Transactions Act, 2017", "features": ["Asset Recovery", "Hidden Ownership"], "dataKey": "be_2017_text" },
        { "title": "Finance Acts", "features": ["Annual Budget", "Tax Reforms"], "dataKey": "fn_acts_text" },
        { "title": "Provincial PST Acts", "features": ["PRA/SRB Rules", "Services Tax"], "dataKey": "pst_acts_text" }
    ],
    "Civil Laws": [
        { "title": "Code of Civil Procedure (CPC), 1908", "features": ["Suits/Decrees", "Court Procedures"], "dataKey": "cpc_1908_text" },
        { "title": "The Contract Act, 1872", "features": ["Agreements", "Remedies"], "dataKey": "co_1872_text" },
        { "title": "The Specific Relief Act, 1877", "features": ["Injunctions", "Specific Performance"], "dataKey": "sr_1877_text" },
        { "title": "The Limitation Act, 1908", "features": ["Time Limits", "Barred Suits"], "dataKey": "li_1908_text" },
        { "title": "The Transfer of Property Act, 1882", "features": ["Conveyance", "Mortgage"], "dataKey": "tp_1882_text" },
        { "title": "The Registration Act, 1908", "features": ["Title Registry", "Document Validity"], "dataKey": "re_1908_text" },
        { "title": "The Guardian and Wards Act, 1890", "features": ["Child Custody", "Welfare"], "dataKey": "gw_1890_text" },
        { "title": "The Defamation Ordinance, 2002", "features": ["Libel/Slander", "Damages"], "dataKey": "de_2002_text" }
    ],
    "Criminal Laws": [
        { "title": "Pakistan Penal Code (PPC), 1860", "features": ["Offenses", "Punishments"], "dataKey": "ppc_1860_text" },
        { "title": "Code of Criminal Procedure (CrPC), 1898", "features": ["Trial/Arrest", "Bail Rules"], "dataKey": "crpc_1898_text" },
        { "title": "Qanun-e-Shahadat Order, 1984", "features": ["Evidence Rules", "Admissibility"], "dataKey": "qs_1984_text" },
        { "title": "Juvenile Justice Act, 2018", "features": ["Minors Rules", "Juvenile Courts"], "dataKey": "jj_2018_text" },
        { "title": "PECA Cybercrime Act, 2016", "features": ["Cyber Crimes", "Data Privacy"], "dataKey": "peca_2016_text" }
    ],
    "Corporate & Commercial Laws": [
        { "title": "Companies Act, 2017", "features": ["Company Law", "Modern Governance"], "dataKey": "co_2017_text" },
        { "title": "Securities Act, 2015", "features": ["Market Logic", "Stock Rules"], "dataKey": "se_2015_text" },
        { "title": "LLP Act, 2017", "features": ["LLP Formation", "Member Liability"], "dataKey": "llp_2017_text" },
        { "title": "Partnership Act, 1932", "features": ["Firm Registry", "Partner Rights"], "dataKey": "pa_1932_text" },
        { "title": "Competition Act, 2010", "features": ["Monopoly Checks", "CCP Authority"], "dataKey": "ca_2010_text" },
        { "title": "Copyright Ordinance, 1962", "features": ["Intellectual Rights", "Artistic Safety"], "dataKey": "cr_1962_text" },
        { "title": "Patents Ordinance, 2000", "features": ["Innovation", "Industry Rights"], "dataKey": "po_2000_text" },
        { "title": "Trademarks Ordinance, 2001", "features": ["Brand Value", "Anti-Faking"], "dataKey": "tm_2001_text" }
    ],
    "Anti-Corruption Laws": [
        { "title": "National Accountability Ordinance, 1999", "features": ["NAB Powers", "Plea Bargains"], "dataKey": "nao_1999_text" },
        { "title": "Prevention of Corruption Act, 1947", "features": ["Bribery Standards", "Public Crimes"], "dataKey": "pca_1947_text" },
        { "title": "FIA Act, 1974", "features": ["Investigative Roles", "Police Powers"], "dataKey": "fia_1974_text" },
        { "title": "Anti-Money Laundering Act, 2010", "features": ["Laundering Checks", "Finance Monitoring"], "dataKey": "aml_2010_text" },
        { "title": "Provincial ACE Rules", "features": ["Regional Corruption", "Punjab/Sindh Rules"], "dataKey": "ace_rules_text" }
    ],
    "Security Laws": [
        { "title": "Anti-Terrorism Act (ATA), 1997", "features": ["Terror Trial", "Special Courts"], "dataKey": "ata_1997_text" },
        { "title": "Protection of Pakistan Act, 2014", "features": ["Detention Powers", "State Safety"], "dataKey": "pop_2014_text" },
        { "title": "Official Secrets Act, 1923", "features": ["Espionage Control", "Classified Info"], "dataKey": "osa_1923_text" },
        { "title": "NACTA Act, 2013", "features": ["National Strategy", "NACTA Strategy"], "dataKey": "nacta_2013_text" }
    ],
    "Anti-Narcotics Laws": [
        { "title": "CNSA Act, 1997", "features": ["Drug Prevention", "Search/Seizure"], "dataKey": "cnsa_1997_text" },
        { "title": "Anti-Narcotics Force Act, 1997", "features": ["ANF Role", "Agency Force"], "dataKey": "anf_1997_text" }
    ],
    "Banking Laws": [
        { "title": "Banking Companies Ordinance, 1962", "features": ["Bank Licensing", "Liquidity"], "dataKey": "bco_1962_text" },
        { "title": "SBP Act, 1956", "features": ["Central Bank", "Monetary Policy"], "dataKey": "sbp_1956_text" },
        { "title": "Recovery of Finances Ordinance, 2001", "features": ["Loan Default", "Recovery Courts"], "dataKey": "rf_2001_text" },
        { "title": "Negotiable Instruments Act, 1881", "features": ["Cheques/Drafts", "Legal Recovery"], "dataKey": "ni_1881_text" },
        { "title": "Microfinance Ordinance, 2001", "features": ["Rural Credit", "Poverty Lending"], "dataKey": "mf_2001_text" }
    ],
    "Police Laws": [
        { "title": "Police Order, 2002", "features": ["Police Reform", "Public Safety"], "dataKey": "po_2002_text" },
        { "title": "Police Act, 1861", "features": ["Old Model", "Discipline Standards"], "dataKey": "pa_1861_text" },
        { "title": "Sindh Police Act, 2019", "features": ["Sindh Policing", "Regional Governance"], "dataKey": "spa_2019_text" },
        { "title": "KP Police Act, 2017", "features": ["KP Strategy", "Department Efficiency"], "dataKey": "kppa_2017_text" }
    ],
    "Specialized Laws": [
        { "title": "Land Acquisition Act, 1894", "features": ["Property Use", "Compensation"], "dataKey": "la_1894_text" },
        { "title": "Industrial Relations Act, 2012", "features": ["Labor Trade Unions", "NIRC Rules"], "dataKey": "ir_2012_text" },
        { "title": "Payment of Wages Act, 1936", "features": ["Wage Security", "Deduction Limits"], "dataKey": "pw_1936_text" },
        { "title": "Environment Protection Act, 1997", "features": ["Pollution Control", "EPA Rules"], "dataKey": "ep_1997_text" }
    ]
};
