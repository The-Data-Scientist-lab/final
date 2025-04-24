import os
import logging
from telethon import TelegramClient, events, Button, types
from dotenv import load_dotenv
import asyncio
from datetime import datetime, timedelta
import random

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the client
client = TelegramClient('bot_session', os.getenv("TELEGRAM_API_ID"), os.getenv("TELEGRAM_API_HASH")).start(bot_token=os.getenv("TELEGRAM_BOT_TOKEN"))

# Model information with enhanced details
MODELS = {
    "model1": {
        "name": "💋 Lucky Rajor",
        "description": """🔥 Nude Content Collection

💫 Original Price: ₹16500 for recorded videos

⭐️ Our Price: ₹750 for 30 minutes lucky rajor video

🎯 Instant Access

✨ Quick Delivery

━━━━━━━━━━━━━━━━━━━━━━━━
📊 Model Statistics
━━━━━━━━━━━━━━━━━━━━━━━━

⭐️ Rating: 4.9/5.0
👥 Orders in last 24 hours: 346
🎯 Success Rate: 100%

━━━━━━━━━━━━━━━━━━━━━━━━
💰 Pricing Plans
━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ Basic Plan (₹750):
- 30 minutes Nude video
- Instant access after payment
- 4K quality
- Basic content collection

⏰ Premium Plan (₹1590):
- 2 Nude videos of 45 minutes each
- Instant access after payment
- 4K quality
- Premium content collection
- 15 Nude Photos Bonus

🎬 VIP Plan (₹3500):
- 4 Nude videos in Black Dress 45 minutes each
- Instant access after payment
- 4K quality
- VIP content collection
- 25 Nude Photos Bonus

💎 Full Package (₹4399):
- 10 Nude Recorded Videos worth of rupees 67000
- Instant access after payment
- 4K quality
- Complete content collection
- 150+ Nude Photos Bonus""",
        "price_basic": 750,
        "price_premium": 1590,
        "price_vip": 3500,
        "price_exclusive": 4399,
        "stats": "👁️ Premium Content | 💖 Instant Delivery",
        "specialties": "HD Videos | 4K Quality | Instant Access",
        "image": os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "luckyrajor.jpg"),
        "original_price": 16500
    },
    "model2": {
        "name": "💝 Miss Pinky (Sana)",
        "description": """✨ Miss Pinky (Sana) Nude Video Collection

💫 Original Price: ₹18500 for recorded videos

💪 Our Price: ₹750 for 30 minutes Nude Video

🏆 Instant Access

🎯 Quick Delivery

━━━━━━━━━━━━━━━━━━━━━━━━
📊 Model Statistics
━━━━━━━━━━━━━━━━━━━━━━━━

⭐️ Rating: 4.8/5.0
👥 Orders in last 24 hours: 287
🎯 Success Rate: 100%

━━━━━━━━━━━━━━━━━━━━━━━━
💰 Pricing Plans
━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ Basic Plan (₹750):
- 30 minutes Nude video
- Instant access after payment
- 4K quality
- Basic content collection

⏰ Premium Plan (₹1590):
- 2 Nude videos of 45 minutes each
- Instant access after payment
- 4K quality
- Premium content collection
- 15 Nude Photos Bonus

🎬 VIP Plan (₹3500):
- 4 Nude videos Removing Black and Red Saree 45 minutes each
- Instant access after payment
- 4K quality
- VIP content collection
- 25 Nude Photos Bonus

💎 Full Package (₹4399):
- 10 Nude Recorded Videos worth of rupees 55000
- Instant access after payment
- 4K quality
- Complete content collection
- 100+ Nude Photos Bonus""",
        "price_basic": 750,
        "price_premium": 1590,
        "price_vip": 3500,
        "price_exclusive": 4399,
        "stats": "👁️ Premium Content | 💖 Instant Delivery",
        "specialties": "HD Videos | 4K Quality | Instant Access",
        "image": os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "Miss Pinky.jpg"),
        "original_price": 18500
    },
    "model3": {
        "name": "✨ Shanaya Katiyan",
        "description": """💫 Shanaya Katiyan Nude Video Collection

⭐️ Original Price: ₹18000 for recorded videos

🎨 Our Price: ₹750 for 30 minutes Nude Video

🏆 Instant Access

✨ Quick Delivery

━━━━━━━━━━━━━━━━━━━━━━━━
📊 Model Statistics
━━━━━━━━━━━━━━━━━━━━━━━━

⭐️ Rating: 4.7/5.0
👥 Orders in last 24 hours: 529
🎯 Success Rate: 100%

━━━━━━━━━━━━━━━━━━━━━━━━
💰 Pricing Plans
━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ Basic Plan (₹750):
- 30 minutes Nude video
- Instant access after payment
- 4K quality
- Basic content collection

⏰ Premium Plan (₹1590):
- 2 Nude videos of 45 minutes each
- Instant access after payment
- 4K quality
- Premium content collection
- 15 Nude Photos Bonus

🎬 VIP Plan (₹3500):
- 4 Nude videos in Sexy and Hot Dresses 45 minutes each
- Instant access after payment
- 4K quality
- VIP content collection
- 25 Nude Photos Bonus

💎 Full Package (₹4399):
- 10 Nude Recorded Videos worth of rupees 73000
- Instant access after payment
- 4K quality
- Complete content collection
- 200+ Nude Photos Bonus""",
        "price_basic": 750,
        "price_premium": 1590,
        "price_vip": 3500,
        "price_exclusive": 4399,
        "stats": "👁️ Premium Content | 💖 Instant Delivery",
        "specialties": "HD Videos | 4K Quality | Instant Access",
        "image": os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "shanaya_katiyan.jpg"),
        "original_price": 18000
    },
    "model4": {
        "name": "💖 Sassy Poonam",
        "description": """✨ Sassy Poonam Nude Video Collection

💫 Original Price: ₹23000 for recorded videos

💪 Our Price: ₹750 for 30 minutes Nude Video

🏆 Instant Access

🎯 Quick Delivery

━━━━━━━━━━━━━━━━━━━━━━━━
📊 Model Statistics
━━━━━━━━━━━━━━━━━━━━━━━━

⭐️ Rating: 4.9/5.0
👥 Orders in last 24 hours: 412
🎯 Success Rate: 100%

━━━━━━━━━━━━━━━━━━━━━━━━
💰 Pricing Plans
━━━━━━━━━━━━━━━━━━━━━━━━

⏱️ Basic Plan (₹750):
- 30 minutes Nude video
- Instant access after payment
- 4K quality
- Basic content collection

⏰ Premium Plan (₹1590):
- 2 Nude videos of 45 minutes each
- Instant access after payment
- 4K quality
- Premium content collection
- 15 Nude Photos Bonus

🎬 VIP Plan (₹3500):
- 4 Nude videos in 2 different Hot top and Dress 45 minutes each
- Total Duration - 3 Hours (45 Minutes each)
- Instant access after payment
- 4K quality
- VIP content collection
- 25 Nude Photos Bonus

💎 Full Package (₹4399):
- 10+ Nude Recorded Videos worth of rupees 67000
- Total Duration - 7+ Hours
- Instant access after payment
- 4K quality
- Complete content collection
- 100+ Nude Photos Bonus""",
        "price_basic": 750,
        "price_premium": 1590,
        "price_vip": 3500,
        "price_exclusive": 4399,
        "stats": "👁️ Premium Content | 💖 Instant Delivery",
        "specialties": "HD Videos | 4K Quality | Instant Access",
        "image": os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "poonam.jpg"),
        "original_price": 23000
    }
}

# Trust indicators
TRUST_INDICATORS = [
    "🔒 Secure Payment Processing",
    "✅ Instant Access After Payment",
    "🛡️ HD Quality Content",
    "📞 Quick Response"
]

# Payment methods
PAYMENT_METHODS = [
    "💳 UPI",
    "🏦 Bank Transfer",
    "📱 PhonePe",
    "💰 Google Pay",
    "💸 Paytm"
]

# Store user selections
user_selections = {}

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a welcome message when the command /start is issued."""
    user = await event.get_sender()
    
    # Initialize user's selection dictionary
    user_selections[user.id] = {
        "model": None,
        "plan": None,
        "price": None,
        "payment_status": None,
        "refund_upi": None
    }
    
    welcome_message = f"""
👋 Hey {user.first_name}!

🎀 Welcome to Premium Content Hub 🎀
⭐️ Premium Content Access

💝 Get Access to Exclusive Content
✨ Instant Delivery
🔥 HD Quality Videos
🎯 4K Resolution Content

━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ IMPORTANT DISCLAIMER ⚠️
━━━━━━━━━━━━━━━━━━━━━━━━

🔞 Age Restriction: 18+ Only
📜 Content: For Personal Use Only
💫 All Content: Professional Quality
🎬 Quick Access: After Payment
✨ Instant Delivery: Guaranteed

━━━━━━━━━━━━━━━━━━━━━━━━
📢 IMPORTANT NOTICE 📢
━━━━━━━━━━━━━━━━━━━━━━━━

💫 I am not the original seller of these videos
💰 Original price is very high 
✨ I am reselling at affordable prices
🎯 Same premium content, lower price


━━━━━━━━━━━━━━━━━━━━━━━━
🚨 URGENT WARNING 🚨
━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ This bot was created on 23rd April 2025
⚠️ Can be banned anytime by Telegram officials
⚠️ Please complete your order as soon as possible
⚠️ Get your content before it's too late

━━━━━━━━━━━━━━━━━━━━━━━━

💋 Choose Your Favorite Collection Below 👇
"""
    buttons = [
        [Button.inline(MODELS["model1"]["name"], b"model1"),
         Button.inline(MODELS["model2"]["name"], b"model2")],
        [Button.inline(MODELS["model3"]["name"], b"model3")],
        [Button.inline(MODELS["model4"]["name"], b"model4")]
    ]
    await event.respond(welcome_message, buttons=buttons, parse_mode='markdown')

@client.on(events.CallbackQuery())
async def callback_handler(event):
    """Handle button presses."""
    data = event.data.decode('utf-8')
    user = await event.get_sender()
    
    # Initialize user's selection dictionary if not exists
    if user.id not in user_selections:
        user_selections[user.id] = {
            "model": None,
            "plan": None,
            "price": None,
            "payment_status": None,
            "refund_upi": None
        }
    
    if data == "back_to_models":
        # Show the model selection menu
        buttons = [
            [Button.inline(MODELS["model1"]["name"], b"model1"),
             Button.inline(MODELS["model2"]["name"], b"model2")],
            [Button.inline(MODELS["model3"]["name"], b"model3")],
            [Button.inline(MODELS["model4"]["name"], b"model4")]
        ]
        await event.respond("💋 Choose Your Favorite Collection Below 👇", buttons=buttons)
        return
    
    elif data.startswith('back_to_plans_') or data.startswith('model'):
        # Handle both back to plans and model selection
        model_id = data.split('_')[-1] if data.startswith('back_to_plans_') else data
        model = MODELS[model_id]
        
        # Update user's selection
        user_selections[user.id]["model"] = model_id
        
        # Split the message into two parts
        short_message = f"""
{model['name']}


💫 Original Price: Starts from ₹{model['original_price']} for recorded videos


⭐️ Our Price: Starts from ₹{model['price_basic']} for 30 minutes


✨ Save: ₹{model['original_price'] - model['price_basic']} ({((model['original_price'] - model['price_basic']) / model['original_price'] * 100):.0f}% OFF)
"""
        
        detailed_message = f"""
{model['description']}

━━━━━━━━━━━━━━━━━━━━━━━━
💳 Choose Your Plan
━━━━━━━━━━━━━━━━━━━━━━━━

Please select your preferred plan below 👇
"""
        
        buttons = [
            [Button.inline(f"⏱️ Basic Plan - ₹{model['price_basic']}", f"plan_{model_id}_basic"),
             Button.inline(f"⏰ Premium Plan - ₹{model['price_premium']}", f"plan_{model_id}_premium")],
            [Button.inline(f"🎬 VIP Plan - ₹{model['price_vip']}", f"plan_{model_id}_vip"),
             Button.inline(f"💎 Full Package - ₹{model['price_exclusive']}", f"plan_{model_id}_exclusive")],
            [Button.inline("🔙 Back to Models", b"back_to_models")]
        ]
        
        try:
            # Get the current working directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Construct the absolute path to the image
            image_path = os.path.join(current_dir, model['image'])
            
            # Log the image path for debugging
            logger.info(f"Attempting to send image from path: {image_path}")
            
            if os.path.exists(image_path):
                # First send the image with short caption
                await event.respond(
                    short_message,
                    file=image_path,
                    parse_mode='markdown'
                )
                logger.info(f"Successfully sent image for model: {model['name']}")
                
                # Then send the detailed message with buttons
                await event.respond(
                    detailed_message,
                    buttons=buttons,
                    parse_mode='markdown'
                )
            else:
                logger.error(f"Image not found at path: {image_path}")
                # If image not found, send text description only
                await event.respond(
                    detailed_message,
                    buttons=buttons,
                    parse_mode='markdown'
                )
        except Exception as e:
            logger.error(f"Error sending image: {str(e)}")
            # If any error occurs, send text description only
            await event.respond(
                detailed_message,
                buttons=buttons,
                parse_mode='markdown'
            )
        return
    
    elif data.startswith('back_to_order_'):
        # Handle back to order navigation
        parts = data.split('_')
        model_id = parts[-2]
        plan_type = parts[-1]
        model = MODELS[model_id]
        
        # Calculate total amount with processing fee
        base_price = model[f"price_{plan_type}"]
        processing_fee = 12
        total_amount = base_price + processing_fee
        
        # Calculate original price based on plan
        original_price = model['original_price']
        savings = original_price - base_price
        savings_percentage = (savings / original_price) * 100
        
        # Get plan name
        plan_names = {
            'basic': 'Basic Plan',
            'premium': 'Premium Plan',
            'vip': 'VIP Plan',
            'exclusive': 'Full Package'
        }
        selected_plan = plan_names[plan_type]
        
        # Show order confirmation
        message = f"""
━━━━━━━━━━━━━━━━━━━━━━━━
🎯 ORDER CONFIRMATION
━━━━━━━━━━━━━━━━━━━━━━━━

💖 Model: {model['name']}
📦 Selected Plan: {selected_plan}

━━━━━━━━━━━━━━━━━━━━━━━━
💰 PRICE DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━

💫 Original Price: ₹{original_price}
⭐️ Our Price: ₹{base_price}
✨ Save: ₹{savings} ({savings_percentage:.0f}% OFF)
💳 Processing Fee: ₹{processing_fee}
💰 Total Amount: ₹{total_amount}

━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ IMPORTANT NOTE
━━━━━━━━━━━━━━━━━━━━━━━━

✅ Please confirm your order
✅ Total amount to pay: ₹{total_amount}
✅ Processing fee included
✅ Instant access after payment

Please confirm your order to proceed to payment.
"""
        buttons = [
            [Button.inline("✅ CONFIRM ORDER", f"confirm_{model_id}_{plan_type}")],
            [Button.inline("🔙 Back to Plans", f"back_to_plans_{model_id}")]
        ]
        await event.respond(message, buttons=buttons, parse_mode='markdown')
        return
    
    elif data.startswith('plan_'):
        # Handle plan selection
        parts = data.split('_')
        model_id = parts[1]
        plan_type = parts[2]
        model = MODELS[model_id]
        
        # Update user's selection
        user_selections[user.id]["model"] = model_id
        user_selections[user.id]["plan"] = plan_type
        user_selections[user.id]["price"] = model[f"price_{plan_type}"]
        
        # Calculate total amount with processing fee
        base_price = model[f"price_{plan_type}"]
        processing_fee = 12
        total_amount = base_price + processing_fee
        
        # Calculate original price based on plan
        original_price = model['original_price']
        savings = original_price - base_price
        savings_percentage = (savings / original_price) * 100
        
        # Get plan name
        plan_names = {
            'basic': 'Basic Plan',
            'premium': 'Premium Plan',
            'vip': 'VIP Plan',
            'exclusive': 'Full Package'
        }
        selected_plan = plan_names[plan_type]
        
        # Show order confirmation
        message = f"""
━━━━━━━━━━━━━━━━━━━━━━━━
🎯 ORDER CONFIRMATION
━━━━━━━━━━━━━━━━━━━━━━━━

💖 Model: {model['name']}
📦 Selected Plan: {selected_plan}

━━━━━━━━━━━━━━━━━━━━━━━━
💰 PRICE DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━

💫 Original Price: ₹{original_price}
⭐️ Our Price: ₹{base_price}
✨ Save: ₹{savings} ({savings_percentage:.0f}% OFF)
💳 Processing Fee: ₹{processing_fee}
💰 Total Amount: ₹{total_amount}

━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ IMPORTANT NOTE
━━━━━━━━━━━━━━━━━━━━━━━━

✅ Please confirm your order
✅ Total amount to pay: ₹{total_amount}
✅ Processing fee included
✅ Instant access after payment

Please confirm your order to proceed to payment.
"""
        buttons = [
            [Button.inline("✅ CONFIRM ORDER", f"confirm_{model_id}_{plan_type}")],
            [Button.inline("🔙 Back to Plans", f"back_to_plans_{model_id}")]
        ]
        await event.respond(message, buttons=buttons, parse_mode='markdown')
    
    elif data.startswith('confirm_'):
        # Handle order confirmation
        parts = data.split('_')
        model_id = parts[1]
        plan_type = parts[2]
        model = MODELS[model_id]
        
        # Calculate total amount with processing fee
        base_price = model[f"price_{plan_type}"]
        processing_fee = 12
        total_amount = base_price + processing_fee
        
        # Get plan name
        plan_names = {
            'basic': 'Basic Plan',
            'premium': 'Premium Plan',
            'vip': 'VIP Plan',
            'exclusive': 'Full Package'
        }
        selected_plan = plan_names[plan_type]
        
        # Show payment QR code
        message = f"""
━━━━━━━━━━━━━━━━━━━━━━━━
💳 PAYMENT DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━

💖 Model: {model['name']}
📦 Selected Plan: {selected_plan}

━━━━━━━━━━━━━━━━━━━━━━━━
💰 PRICE DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━

💫 Original Price: ₹{model['original_price']}
⭐️ Our Price: ₹{base_price}
💳 Processing Fee: ₹{processing_fee}
💰 Total Amount: ₹{total_amount}

━━━━━━━━━━━━━━━━━━━━━━━━
📝 PAYMENT INSTRUCTIONS
━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ Scan the QR code below
2️⃣ Pay the exact amount: ₹{total_amount}
3️⃣ Take a screenshot of payment
4️⃣ Send the screenshot to this chat
5️⃣ Get instant access to content

━━━━━━━━━━━━━━━━━━━━━━━━
🚀 INSTANT ACCESS
━━━━━━━━━━━━━━━━━━━━━━━━

✅ You will receive Google Drive links within seconds
✅ Download videos instantly
✅ No waiting time
✅ HD Quality Content

━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ IMPORTANT
━━━━━━━━━━━━━━━━━━━━━━━━

✅ Pay exact amount only
✅ Include transaction ID in screenshot
✅ Clear screenshot required
✅ Instant access after verification
"""
        buttons = [[Button.inline("🔙 Back to Order", f"back_to_order_{model_id}_{plan_type}")]]
        
        try:
            # Get absolute path of the QR code
            qr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "QR.jpg")
            
            if os.path.exists(qr_path):
                # Send QR code with payment message
                await event.respond(
                    message,
                    file=qr_path,
                    buttons=buttons,
                    parse_mode='markdown'
                )
            else:
                await event.respond("⚠️ QR code not found. Please contact support.")
        except Exception as e:
            await event.respond(f"⚠️ Error displaying QR code: {str(e)}")

@client.on(events.NewMessage(func=lambda e: e.photo))
async def handle_photo(event):
    """Handle the payment screenshot."""
    user = await event.get_sender()
    
    # Initialize user's selection dictionary if not exists
    if user.id not in user_selections:
        user_selections[user.id] = {
            "model": None,
            "plan": None,
            "price": None,
            "payment_status": None,
            "refund_upi": None
        }
    
    # Update payment status
    user_selections[user.id]["payment_status"] = "Payment Screenshot Received"
    
    # Get user's selected model and plan
    model_id = user_selections[user.id]["model"]
    plan_type = user_selections[user.id]["plan"]
    
    if not all([model_id, plan_type]):
        await event.respond("⚠️ Error: Missing order information. Please start over.")
        return
        
    await event.respond(f"""
━━━━━━━━━━━━━━━━━━━━━━━━
💫 Payment Verification Started 💫
━━━━━━━━━━━━━━━━━━━━━━━━

✅ Payment screenshot received successfully!
⏳ Starting verification process...

🔍 Status: Processing

✨ Please wait while we verify your payment
🎯 We'll notify you in just a few seconds
💖 Thank you for your patience
""", parse_mode='markdown')
        
    # Wait for 12 seconds
    await asyncio.sleep(12)
    
    # Update payment status
    user_selections[user.id]["payment_status"] = "Payment Verification Failed"
    
    # Send failed payment message
    await event.respond(f"""
━━━━━━━━━━━━━━━━━━━━━━━━
❌ Payment Verification Failed ❌
━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ Your payment could not be verified
❌ Please try again with a clear screenshot
💫 Make sure the transaction details are visible

━━━━━━━━━━━━━━━━━━━━━━━━
📝 What to do next?
━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ Take a clear screenshot of your payment
2️⃣ Make sure transaction ID is visible
3️⃣ Send the screenshot again
4️⃣ We'll verify it within seconds

━━━━━━━━━━━━━━━━━━━━━━━━
💫 IMPORTANT NOTE 💫
━━━━━━━━━━━━━━━━━━━━━━━━

✅ Clear screenshot required
✅ Transaction ID must be visible
✅ Amount must match exactly
✅ Try again with better quality

━━━━━━━━━━━━━━━━━━━━━━━━
💖 SUPPORT MESSAGE 💖
━━━━━━━━━━━━━━━━━━━━━━━━

If you are still facing issues with your payment, don't worry! We are here to help you. You will receive updates within the next three hours. Our support team is working to resolve your issue and ensure you get access to your content.

Thank you for your patience and understanding.
""", parse_mode='markdown')

    # Wait for 3 hours (10800 seconds)
    await asyncio.sleep(10800)
    
    # Send update message with refund option
    buttons = [
        [Button.inline("💰 REQUEST REFUND", b"request_refund")],
        [Button.inline("⏳ CONTINUE WAITING", b"continue_waiting")]
    ]
    
    await event.respond(f"""
━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ PAYMENT VERIFICATION UPDATE ⚠️
━━━━━━━━━━━━━━━━━━━━━━━━

Dear {user.first_name},

🔴 WE ARE STILL FACING ISSUES VERIFYING YOUR PAYMENT
🟡 OUR TEAM IS WORKING DILIGENTLY ON THIS MATTER

⏳ EXPECTED VERIFICATION TIME: UP TO 3 DAYS
🔍 CURRENT STATUS: UNDER REVIEW

━━━━━━━━━━━━━━━━━━━━━━━━
💰 REFUND OPTION AVAILABLE 💰
━━━━━━━━━━━━━━━━━━━━━━━━

If you prefer not to wait, you can request a refund by clicking the button below.
Your money will be refunded within 7 days after verification.

Please choose your preferred option:
""", buttons=buttons, parse_mode='markdown')

@client.on(events.CallbackQuery(pattern=r'continue_waiting'))
async def handle_continue_waiting(event):
    """Handle users who choose to continue waiting."""
    user = await event.get_sender()
    
    await event.respond("""
━━━━━━━━━━━━━━━━━━━━━━━━
⏳ VERIFICATION CONTINUING ⏳
━━━━━━━━━━━━━━━━━━━━━━━━

Thank you for your patience!

💫 We will continue processing your payment
✨ You will receive updates as soon as available
🎯 Our team is working to resolve this quickly

We appreciate your understanding and cooperation.
""", parse_mode='markdown')
    
    # Wait for 7 hours (25200 seconds)
    await asyncio.sleep(25200)
    
    # Send update message after 7 hours
    buttons = [
        [Button.inline("💰 REQUEST REFUND", b"request_refund")]
    ]
    
    await event.respond(f"""
━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ PAYMENT VERIFICATION UPDATE ⚠️
━━━━━━━━━━━━━━━━━━━━━━━━

Dear {user.first_name},

🔴 WE ARE STILL VERIFYING YOUR PAYMENT
🟡 PLEASE BE PATIENT AS THIS PROCESS TAKES TIME

⏳ VERIFICATION STATUS: IN PROGRESS
🔍 ESTIMATED TIME: 24-48 HOURS

━━━━━━━━━━━━━━━━━━━━━━━━
💰 REFUND OPTION STILL AVAILABLE 💰
━━━━━━━━━━━━━━━━━━━━━━━━

If you wish to cancel the verification and request a refund,
you can do so by clicking the button below.

Your money will be refunded within 7 days after verification.
""", buttons=buttons, parse_mode='markdown')

@client.on(events.CallbackQuery(pattern=r'request_refund'))
async def handle_refund_request(event):
    """Handle refund requests."""
    user = await event.get_sender()
    
    await event.respond("""
━━━━━━━━━━━━━━━━━━━━━━━━
💰 REFUND REQUEST FORM 💰
━━━━━━━━━━━━━━━━━━━━━━━━

Please enter your UPI ID or Phone Number for the refund.
Format: `upi:yourname@bank` or `phone:1234567890`

Example:
`upi:john@okicici`
`phone:9876543210`

Reply to this message with your details.
""", parse_mode='markdown')
    
    # Set user state to waiting for UPI
    user_selections[user.id]["payment_status"] = "awaiting_refund_details"

@client.on(events.NewMessage(pattern=r'^(upi|phone):'))
async def handle_refund_details(event):
    """Handle refund details submission."""
    user = await event.get_sender()
    
    if user.id in user_selections and user_selections[user.id]["payment_status"] == "awaiting_refund_details":
        refund_details = event.text
        parts = refund_details.split(':')
        type = parts[0].lower()
        value = parts[1].strip()
        
        # Validate phone number
        if type == 'phone':
            # Remove any spaces or special characters
            phone = ''.join(filter(str.isdigit, value))
            if not (10 <= len(phone) <= 11):
                await event.respond("""
━━━━━━━━━━━━━━━━━━━━━━━━
❌ INVALID PHONE NUMBER ❌
━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ Your phone number must be 10 or 11 digits
❌ Please enter a valid phone number
💫 Format: phone:1234567890

Example:
phone:9876543210

Please try again with a valid phone number.
""", parse_mode='markdown')
                return
        
        # Validate UPI ID
        elif type == 'upi':
            if not (value.endswith('@okbank') or value.endswith('@okicici') or value.endswith('@oksbi') or 
                   value.endswith('@okhdfcbank') or value.endswith('@okaxis') or value.endswith('@okbob')):
                await event.respond("""
━━━━━━━━━━━━━━━━━━━━━━━━
❌ INVALID UPI ID ❌
━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ Your UPI ID must be in the correct format
❌ Please enter a valid UPI ID
💫 Format: upi:username@bankname

Examples:
upi:john@okicici
upi:jane@oksbi
upi:user@okhdfcbank

Supported banks:
- @okicici
- @oksbi
- @okhdfcbank
- @okaxis
- @okbob
- @okbank

Please try again with a valid UPI ID.
""", parse_mode='markdown')
                return
        
        # If validation passes, proceed with the refund request
        user_selections[user.id]["refund_upi"] = refund_details
        user_selections[user.id]["payment_status"] = "refund_requested"
        
        await event.respond("""
━━━━━━━━━━━━━━━━━━━━━━━━
✅ REFUND REQUEST RECEIVED ✅
━━━━━━━━━━━━━━━━━━━━━━━━

Thank you for providing your refund details!

💫 Your refund request has been registered
⏳ Processing Time: Up to 7 days
✅ You will receive the refund once verified

We appreciate your patience and understanding.
Thank you for giving us the opportunity to serve you.

━━━━━━━━━━━━━━━━━━━━━━━━
💝 Stay Connected 💝
━━━━━━━━━━━━━━━━━━━━━━━━

Feel free to contact us for any queries.
We value your trust and hope to serve you better in the future!
""", parse_mode='markdown')
        
        # Wait for 8 hours (28800 seconds)
        await asyncio.sleep(28800)
        
        # Send verification update after 8 hours
        await event.respond(f"""
━━━━━━━━━━━━━━━━━━━━━━━━
✅ REFUND VERIFICATION UPDATE ✅
━━━━━━━━━━━━━━━━━━━━━━━━

Dear {user.first_name},

💫 YOUR REFUND VERIFICATION HAS BEGUN
✨ WE ARE CURRENTLY VERIFYING YOUR PAYMENT
🎯 ONCE VERIFIED, YOU WILL RECEIVE YOUR REFUND

⏳ REFUND PROCESSING TIME: WITHIN 7 DAYS
🔍 CURRENT STATUS: VERIFICATION IN PROGRESS

━━━━━━━━━━━━━━━━━━━━━━━━
💖 THANK YOU FOR YOUR PATIENCE 💖
━━━━━━━━━━━━━━━━━━━━━━━━

We are working diligently to process your refund.
You will receive another update once the verification is complete.
""", parse_mode='markdown')

async def main():
    """Start the bot."""
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main()) 