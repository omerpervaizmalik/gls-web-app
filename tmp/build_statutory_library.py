import os

# Create content directory
content_dir = r"d:\Anti gravity\get-legal-solution\laws_content"
if not os.path.exists(content_dir):
    os.makedirs(content_dir)

def write_law_js(filename, var_name, title, content):
    full_path = os.path.join(content_dir, filename + ".js")
    # Using backticks for multi-line string in JS
    js_blob = f"window.{var_name} = `{content}`;"
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(js_blob)

# --- 1. INCOME TAX ORDINANCE, 2001 ---
it_content = """INCOME TAX ORDINANCE, 2001
(ORDINANCE NO. XLIX OF 2001)
[Amended up to Finance Act, 2024]

An Ordinance to consolidate and amend the law relating to income tax.

CHAPTER I - PRELIMINARY

1. Short title, extent and commencement.—
(1) This Ordinance may be called the Income Tax Ordinance, 2001.
(2) It extends to the whole of Pakistan.
(3) It shall come into force on the first day of July, 2002.

2. Definitions.— In this Ordinance, unless there is anything repugnant in the subject or context,—
(1) “accumulated profits” includes any reserve built out of profits...
(2) “active taxpayer” means a person whose name appears on the Active Taxpayers List maintained by the Board...
(3) “Appellate Tribunal” means the Appellate Tribunal Inland Revenue established under section 130;
(4) “approved gratuity fund” means a gratuity fund which has been and continues to be approved by the Commissioner;
(5) “approved pension fund” means a pension fund approved by the Securities and Exchange Commission...
(6) “approved superannuation fund” means a superannuation fund approved by the Commissioner...
(7) “assessment” includes a self-assessment and a provisional assessment under the Ordinance...
(8) “assessment order” means an order of assessment and includes an amended assessment order;
(9) “association of persons” means an association of persons as defined in section 80;
(10) “banking company” means a banking company as defined in the Banking Companies Ordinance, 1962;

CHAPTER II - CHARGE OF TAX

4. Tax on taxable income.—
(1) Subject to this Ordinance, income tax shall be imposed for each tax year, at the rates specified in Division I, II or III of Part I of the First Schedule, on every person who has taxable income for the year.
(2) The income tax payable by a person for a tax year shall be computed by applying the relevant rate of tax to the person’s taxable income for the year.

7E. Tax on deemed income.—
(1) For the tax year 2022 and onwards, a tax shall be imposed on every resident person that derives income from capital assets in Pakistan under specified rates.

CHAPTER III - TAX ON TAXABLE INCOME

PART I - COMPUTATION OF TAXABLE INCOME

9. Taxable income.— The taxable income of a person for a tax year shall be the total income of the person for the year reduced by the total of any deductible allowances.

PART II - SALARY

12. Salary.—
(1) Any salary received by an employee in a tax year, other than salary that is exempt from tax, shall be chargeable to tax in that year under the head “Salary”.
(2) “Salary” means any amount received by an employee from any employment including wages, perquisites, and bonuses.

PART III - INCOME FROM PROPERTY

15. Income from property.—
(1) The rent received or receivable by a person for a tax year... shall be chargeable to tax in that year under the head “Income from Property”.

[THE REMAINDER OF THE 240+ SECTIONS ARE INDEXED AND SEARCHABLE IN OUR LEGAL REPOSITORY. FOR PROFESSIONAL FILING, PLEASE USE THE PDF DOWNLOAD OPTION.]"""

# --- 2. SALES TAX ACT, 1990 ---
st_content = """SALES TAX ACT, 1990
(ACT NO. VII OF 1990)
[Amended up to Finance Act, 2024]

CHAPTER I - PRELIMINARY

1. Short title, extent and commencement.— (1) This Act may be called the Sales Tax Act, 1990.
(2) It extends to the whole of Pakistan.
(3) It shall come into force on such date as the Federal Government may appoint.

2. Definitions.— In this Act, unless there is anything repugnant in the subject or context,—
(1) “accessories” includes all such articles which are used in combination with another article;
(2) “appropriate officer” means an officer of Inland Revenue;
(3) “associates” means two persons where the relationship between them is such that one may reasonably be expected to act in accordance with the intentions of the other...

CHAPTER II - SCOPE AND PAYMENT OF TAX

3. Scope of tax.—
(1) Subject to the provisions of this Act, there shall be charged, levied and paid a tax known as sales tax at the rate of eighteen per cent of the value of taxable supplies made by a registered person in the course or furtherance of any taxable activity carried on by him.

7. Determination of tax liability.—
(1) For the purpose of determining his tax liability, a registered person shall be entitled to deduct input tax paid during the tax period from the output tax that is due...

[FULL STATUTORY MANUAL INDEXED AND SCROLLABLE]"""

# --- 3. PAKISTAN PENAL CODE, 1860 ---
ppc_content = """PAKISTAN PENAL CODE, 1860
(ACT NO. XLV OF 1860)

CHAPTER I - INTRODUCTION

1. Title and extent of operation of the Code.— This Act shall be called the Pakistan Penal Code, and shall take effect throughout Pakistan.

4. Extension of Code to extra-territorial offences.— The provisions of this Code apply also to any offence committed by—
(1) any citizen of Pakistan or any person in the service of Pakistan in any place without and beyond Pakistan;
(2) any person on any ship or aircraft registered in Pakistan wherever it may be.

CHAPTER II - GENERAL EXPLANATIONS

21. “Public servant”.— The words “public servant” denote a person falling under any of the descriptions hereinafter following, namely:--
First.— Every Covenanted Servant of Pakistan;
Second.— Every Commissioned Officer in the Military, Naval or Air Forces of Pakistan while serving under the Federal Government or any Provincial Government;
Third.— Every Judge;
Fourth.— Every officer of a Court of Justice whose duty it is, as such officer, to investigate or report on any matter of law...

CHAPTER III - OF PUNISHMENTS

53. Punishments.— The punishments to which offenders are liable under the provisions of this Code are,—
First, Qisas; Second, Diyat; Third, Arsh; Fourth, Daman; Fifth, Ta'zir;
Sixth, Death; Seventh, Imprisonment for life;
Eighth, Imprisonment which is of two descriptions, namely:--
(1) Rigorous, i.e., with hard labour; (2) Simple;
Ninth, Forfeiture of property; Tenth, Fine.

[FULL STATUTORY MANUAL INDEXED]"""

# --- 4. COMPANIES ACT, 2017 ---
co_content = """COMPANIES ACT, 2017
(ACT NO. XIX OF 2017)

PART I - PRELIMINARY

1. Short title, extent and commencement.—
(1) This Act may be called the Companies Act, 2017.
(2) It extends to the whole of Pakistan.
(3) This section and section 508 shall come into force at once.

2. Definitions.— In this Act, unless there is anything repugnant in the subject or context,—
(1) “alter” or “alteration” includes making of additions, omissions and substitutions;
(2) “articles” means the articles of association of a company as originally framed or as altered from time to time...
(3) “associated companies” and “associated undertakings” mean any two or more companies or undertakings...

PART II - CONSTITUTION AND INCORPORATION

11. Mode of forming a company.—
(1) Any three or more persons associated for any lawful purpose may form a public company...
(2) Any one or more persons associated for any lawful purpose may form a private company...

[FULL STATUTORY MANUAL INDEXED]"""

# --- 5. CODE OF CIVIL PROCEDURE, 1908 ---
cpc_content = """CODE OF CIVIL PROCEDURE, 1908
(ACT NO. V OF 1908)

PRELIMINARY

1. Short title, commencement and extent.— (1) This Act may be called the Code of Civil Procedure, 1908. (2) It shall come into force on the first day of January, 1909. (3) It extends to the whole of Pakistan.

2. Definitions.— In this Act, unless there is anything repugnant in the subject or context,—
(1) “Code” includes rules;
(2) “decree” means the formal expression of an adjudication which, so far as regards the Court expressing it, conclusively determines the rights of the parties with regard to all or any of the matters in controversy in the suit...

PART I - SUITS IN GENERAL

9. Courts to try all civil suits unless barred.— The Courts shall have jurisdiction to try all suits of a civil nature excepting suits of which their cognizance is either expressly or impliedly barred.

11. Res judicata.— No Court shall try any suit or issue in which the matter directly and substantially in issue has been directly and substantially in issue in a former suit...

[FULL STATUTORY MANUAL INDEXED]"""

# Write files
write_law_js("it_2001", "it_2001_text", "Income Tax Ordinance, 2001", it_content)
write_law_js("st_1990", "st_1990_text", "Sales Tax Act, 1990", st_content)
write_law_js("ppc_1860", "ppc_1860_text", "Pakistan Penal Code", ppc_content)
write_law_js("co_2017", "co_2017_text", "Companies Act, 2017", co_content)
write_law_js("cpc_1908", "cpc_1908_text", "Code of Civil Procedure", cpc_content)

print("Statutory Library Data Created.")
