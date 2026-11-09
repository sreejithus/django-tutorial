from google import genai
api_key="AIzaSyC04p986dY9YsWCxfCJBE0QM0UsOU7wpCw"

client = genai.Client(api_key=api_key)



def get_budget_plan(response_data):
               monthly_expense = response_data.get('monthly_total')
               category_total = response_data.get('category_expense_month')
               categorysummarytext=""
               for i in category_total:
                            categorysummarytext += f"{i.get('category')}-{i.get('total')}"




               prompt = f"""
                             Act as an expert financial advisor specializing in family budgeting and pers

                             Here is my monthly financial summary for last month:
                             - Total Monthly Expense: ₹{monthly_expense}
                             - Category Breakdown: {categorysummarytext}


                              Based on this data, please provide a practical 1-month  budget plan:
                              1. *Expense Analysis: Point out high-spending areas relative to typical Kerala cost of living.
                              2. Optimized 1-Month Allocation Plan: Suggest a revised budget breakdown.
                              3. Actionable Kerala-Specific Savings Tips:* Provide 3-4 realistic ways to cut costs in Kerala.
                               """





               response = client.models.generate_content(
                              model="gemini-3.5-flash",
                           contents=prompt
                                        )

               response_data['budget_plan'] = response.text
               return response_data