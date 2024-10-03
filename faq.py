faq_data = {
    "What types of properties do you offer?": "We offer a variety of properties including residential, commercial, and industrial real estate.",
    "What is the average return on investment for your properties?": "The average ROI for our properties ranges from 5% to 10% annually, depending on the location and type of property.",
    "Can I visit the property before making a purchase?": "Yes, we encourage potential investors to visit the property and inspect it before making a purchase.",
    "Do you provide property management services?": "Yes, we offer comprehensive property management services to ensure your investment is well-maintained.",
    "What financing options are available?": "We have partnerships with several financial institutions to offer competitive mortgage rates and financing options.",
    "Are there any hidden fees I should be aware of?": "We are transparent with all costs involved. Any additional fees will be clearly outlined in the purchase agreement.",
    "What is the process for purchasing a property?": "The process involves property selection, financing approval, contract signing, and closing. We guide you through each step.",
    "Can I see a detailed financial analysis of the property?": "Yes, we provide a comprehensive financial analysis for each property, including projected cash flow and potential appreciation.",
    "What is the typical duration of the closing process?": "The closing process usually takes 30 to 45 days, depending on the complexity of the transaction.",
    "Do you offer properties in different geographical locations?": "Yes, we have a diverse portfolio of properties across various regions and cities.",
    "What is the occupancy rate of your properties?": "Our properties have an average occupancy rate of 95%, indicating high demand and stable income potential.",
    "Can I customize or renovate the property after purchase?": "Yes, you can customize or renovate the property according to your needs, subject to local regulations and property type.",
    "What is the average appreciation rate for your properties?": "Our properties typically appreciate at a rate of 3% to 6% annually, depending on market conditions.",
    "Do you provide assistance with tenant placement?": "Yes, we assist with tenant placement to ensure your property generates rental income quickly.",
    "What are the property taxes and insurance costs?": "Property taxes and insurance costs vary by location and property type. We provide detailed estimates for each property.",
    "Can I use the property for personal use?": "Yes, depending on the property type and terms of the purchase agreement, you can use the property for personal purposes.",
    "What are the maintenance costs associated with the property?": "Maintenance costs vary by property type and location. We provide detailed estimates and offer property management services to handle maintenance.",
    "Do you offer any guarantees on rental income?": "While we do not offer guarantees, our properties have a high occupancy rate and stable rental demand, minimizing vacancy risks.",
    "Can I sell the property at any time?": "Yes, you can sell the property at any time. We can assist with the resale process to ensure a smooth transaction.",
    "What legal support do you provide during the purchase?": "We provide comprehensive legal support, including contract preparation and review, to ensure a secure transaction.",
    "How do you determine the market value of a property?": "We use a combination of market analysis, comparable property sales, and professional appraisals to determine market value.",
    "What is the minimum investment required?": "The minimum investment required varies by property. We offer options suitable for different investment budgets.",
    "Do you have properties with existing tenants?": "Yes, we offer properties with existing tenants, providing immediate rental income for investors.",
    "What is the expected rental yield?": "The expected rental yield for our properties ranges from 4% to 8% annually, depending on location and property type.",
    "How do you handle property disputes?": "We have a dedicated legal team to handle any property disputes and ensure your investment is protected.",
    "Can I invest in multiple properties?": "Yes, you can diversify your investment by purchasing multiple properties from our portfolio.",
    "What is the vacancy rate for your properties?": "Our properties have a low vacancy rate, typically below 5%, indicating strong rental demand.",
    "Do you offer properties for short-term rentals?": "Yes, we have properties suitable for short-term rentals, ideal for vacation or corporate housing.",
    "What kind of support do you offer after the purchase?": "We offer ongoing support, including property management, tenant placement, and maintenance services.",
    "How do you ensure the quality of the properties?": "All properties undergo thorough inspections and due diligence to ensure they meet our high standards."
}

def get_faq_response(question):
    return faq_data.get(question, "Sorry, I don't have an answer to that question. Please contact our customer support for more information.")
