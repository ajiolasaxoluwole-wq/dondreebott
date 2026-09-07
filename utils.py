import math
from datetime import datetime, timedelta
import re
from fractions import Fraction

class CalculatorUtils:
    
    @staticmethod
    def basic_calc(expression: str) -> str:
        """Perform basic arithmetic operations"""
        try:
            expression = expression.replace('×', '*').replace('÷', '/')
            if not re.match(r'^[\d+\-*/().\s]+$', expression):
                return "❌ Invalid expression! Use only numbers and + - × ÷ ( )"
            
            result = eval(expression)
            return f"✅ Result: {result}"
        except ZeroDivisionError:
            return "❌ Division by zero is not allowed!"
        except Exception:
            return "❌ Invalid expression! Please check your input."
    
    @staticmethod
    def percentage_calc(number: float, percentage: float) -> str:
        """Calculate percentage of a number"""
        result = (percentage / 100) * number
        return f"✅ {percentage}% of {number} = {result:.2f}"
    
    @staticmethod
    def fraction_calc(operation: str, num1: int, den1: int, num2: int, den2: int) -> str:
        """Perform fraction operations"""
        try:
            frac1 = Fraction(num1, den1)
            frac2 = Fraction(num2, den2)
            
            if operation == '+':
                result = frac1 + frac2
            elif operation == '-':
                result = frac1 - frac2
            elif operation == '*':
                result = frac1 * frac2
            elif operation == '/':
                result = frac1 / frac2
            else:
                return "❌ Invalid operation! Use +, -, *, /"
            
            return f"✅ {frac1} {operation} {frac2} = {result} ({float(result):.4f})"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    @staticmethod
    def average_calc(numbers: list) -> str:
        """Calculate average of numbers"""
        try:
            total = sum(numbers)
            avg = total / len(numbers)
            return f"✅ Average = {avg:.2f}\n📊 Sum = {total}\n🔢 Count = {len(numbers)}"
        except Exception:
            return "❌ Invalid input! Please provide numbers separated by spaces."
    
    @staticmethod
    def discount_calc(price: float, discount: float) -> str:
        """Calculate discount"""
        discount_amount = (discount / 100) * price
        final_price = price - discount_amount
        return f"""✅ Discount Details:
💵 Original Price: ${price:.2f}
🎯 Discount: {discount}%
💰 Discount Amount: ${discount_amount:.2f}
💳 Final Price: ${final_price:.2f}
🤑 You Save: ${discount_amount:.2f}"""
    
    @staticmethod
    def age_calc(birth_date: str) -> str:
        """Calculate age from birth date (YYYY-MM-DD)"""
        try:
            birth = datetime.strptime(birth_date, "%Y-%m-%d")
            today = datetime.now()
            
            if birth > today:
                return "❌ Birth date cannot be in the future!"
            
            years = today.year - birth.year
            months = today.month - birth.month
            days = today.day - birth.day
            
            if days < 0:
                months -= 1
                days += 30
            if months < 0:
                years -= 1
                months += 12
            
            total_days = (today - birth).days
            next_birthday = datetime(today.year, birth.month, birth.day)
            if next_birthday < today:
                next_birthday = datetime(today.year + 1, birth.month, birth.day)
            days_until = (next_birthday - today).days
            
            return f"""✅ Age Calculator:
📅 Birth Date: {birth_date}
👤 Age: {years} years, {months} months, {days} days
📆 Total Days Lived: {total_days:,} days
🎂 Next Birthday: {days_until} days to go!"""
        except ValueError:
            return "❌ Invalid date format! Use YYYY-MM-DD"
    
    @staticmethod
    def date_calc(date1: str, date2: str) -> str:
        """Calculate difference between two dates"""
        try:
            d1 = datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.strptime(date2, "%Y-%m-%d")
            
            diff = abs(d2 - d1)
            days = diff.days
            weeks = days // 7
            months = days // 30
            years = days // 365
            
            return f"""✅ Date Difference:
📅 Date 1: {date1}
📅 Date 2: {date2}
⏱️ Difference:
• {days} days
• {weeks} weeks
• {months} months (approx)
• {years} years (approx)"""
        except ValueError:
            return "❌ Invalid date format! Use YYYY-MM-DD"

class UnitConverter:
    
    @staticmethod
    def length_convert(value: float, from_unit: str, to_unit: str) -> str:
        """Convert between length units"""
        units = {
            'mm': 0.001,
            'cm': 0.01,
            'm': 1.0,
            'km': 1000.0,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.344
        }
        
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in units or to_unit not in units:
            return "❌ Invalid unit! Available: mm, cm, m, km, in, ft, yd, mi"
        
        try:
            in_meters = value * units[from_unit]
            result = in_meters / units[to_unit]
            return f"✅ {value} {from_unit} = {result:.6f} {to_unit}"
        except Exception:
            return "❌ Conversion failed!"
    
    @staticmethod
    def weight_convert(value: float, from_unit: str, to_unit: str) -> str:
        """Convert between weight units"""
        units = {
            'mg': 0.000001,
            'g': 0.001,
            'kg': 1.0,
            'ton': 1000.0,
            'oz': 0.0283495,
            'lb': 0.453592
        }
        
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in units or to_unit not in units:
            return "❌ Invalid unit! Available: mg, g, kg, ton, oz, lb"
        
        try:
            in_kg = value * units[from_unit]
            result = in_kg / units[to_unit]
            return f"✅ {value} {from_unit} = {result:.6f} {to_unit}"
        except Exception:
            return "❌ Conversion failed!"
    
    @staticmethod
    def temperature_convert(value: float, from_unit: str, to_unit: str) -> str:
        """Convert between temperature units"""
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()
        
        try:
            if from_unit == 'C' and to_unit == 'F':
                result = (value * 9/5) + 32
            elif from_unit == 'F' and to_unit == 'C':
                result = (value - 32) * 5/9
            elif from_unit == 'C' and to_unit == 'K':
                result = value + 273.15
            elif from_unit == 'K' and to_unit == 'C':
                result = value - 273.15
            elif from_unit == 'F' and to_unit == 'K':
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == 'K' and to_unit == 'F':
                result = (value - 273.15) * 9/5 + 32
            else:
                return "❌ Invalid conversion! Use C, F, or K"
            
            return f"✅ {value}°{from_unit} = {result:.2f}°{to_unit}"
        except Exception:
            return "❌ Conversion failed!"

# Initialize utilities
calc_utils = CalculatorUtils()
unit_converter = UnitConverter()
