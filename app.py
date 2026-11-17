from flask import Flask, render_template, abort

app = Flask(__name__)

# Master dictionary holding all bilingual app data and detailed step-by-step guides
DATA = {
    'en': {
        'nav_home': 'Home',
        'nav_guides': 'Guides',
        'switch_lang_code': 'np',
        'switch_lang_btn': '🇳🇵 नेपाली',
        'select_app_title': 'Select an App',
        'search_placeholder': 'Search app (e.g., Facebook, WhatsApp)...',
        'read_aloud_btn': '🔊 Listen to Guide',
        'back_btn': '⬅ Back to Apps',
        'apps': [
            {'id': 'facebook', 'title': 'Facebook & Messenger', 'icon': '📘'},
            {'id': 'whatsapp', 'title': 'WhatsApp', 'icon': '🟢'},
            {'id': 'instagram', 'title': 'Instagram', 'icon': '📷'},
            {'id': 'viber', 'title': 'Viber', 'icon': '💜'},
            {'id': 'phone', 'title': 'Phone & Contacts', 'icon': '📞'}
        ],
        'guides': {
            'facebook': {
                'title': 'Facebook & Messenger Guide',
                'steps': [
                    {
                        'title': '1. Create New Account',
                        'text': 'Open Facebook and tap "Create new account" at the bottom.',
                        'speech': 'Step 1: Open Facebook and tap Create new account at the bottom.',
                        'images': ['fb_step1_1.png']
                    },
                    {
                        'title': '2. Enter Your Name',
                        'text': 'Type your First Name and Last Name into the boxes, then tap Next.',
                        'speech': 'Step 2: Type your First Name and Last Name into the boxes then tap Next.',
                        'images': ['fb_step1_2.png']
                    },
                    {
                        'title': '3. Select Date of Birth',
                        'text': 'Select your birthday and tap Next.',
                        'speech': 'Step 3: Select your birthday and tap Next.',
                        'images': ['fb_step1_3.png']
                    },
                    {
                        'title': '4. Choose Gender',
                        'text': 'Select your gender option and tap Next.',
                        'speech': 'Step 4: Select your gender option and tap Next.',
                        'images': ['fb_step1_4.png']
                    },
                    {
                        'title': '5. Enter Phone Number',
                        'text': 'Type your mobile number and tap Next.',
                        'speech': 'Step 5: Type your mobile number and tap Next.',
                        'images': ['fb_step1_5.png']
                    },
                    {
                        'title': '6. Create Password',
                        'text': 'Create a secure password and tap Sign Up.',
                        'speech': 'Step 6: Create a secure password and tap Sign Up.',
                        'images': ['fb_step1_6.png']
                    }
                ]
            },
            'whatsapp': {
                'title': 'WhatsApp Setup Guide',
                'steps': [
                    {
                        'title': '1. Open WhatsApp',
                        'text': 'Open WhatsApp from your phone home screen.',
                        'speech': 'Step 1: Open WhatsApp from your phone home screen.',
                        'images': ['wa_step1.png']
                    },
                    {
                        'title': '2. Agree & Continue',
                        'text': 'Tap "Agree and Continue" to accept the terms.',
                        'speech': 'Step 2: Tap Agree and Continue to accept the terms.',
                        'images': ['wa_step2.png']
                    },
                    {
                        'title': '3. Allow Permissions',
                        'text': 'Tap "Allow" when asked for contacts and notifications.',
                        'speech': 'Step 3: Tap Allow when asked for contacts and notifications.'
                    },
                    {
                        'title': '4. Enter Phone Number',
                        'text': 'Select your country and enter your mobile phone number.',
                        'speech': 'Step 4: Select your country and enter your mobile phone number.',
                        'images': ['wa_step4.png']
                    },
                    {
                        'title': '5. Verify Number',
                        'text': 'Enter the 6-digit code sent to you via SMS.',
                        'speech': 'Step 5: Enter the 6-digit code sent to you via SMS.'
                    },
                    {
                        'title': '6. Profile Setup',
                        'text': 'Type your name and add a profile photo.',
                        'speech': 'Step 6: Type your name and add a profile photo.',
                        'images': ['wa_step6.png']
                    }
                ]
            },
            'instagram': {
                'title': 'Instagram Setup Guide',
                'steps': [
                    {
                        'title': '1. Open Instagram',
                        'text': 'Open the Instagram app on your mobile device.',
                        'speech': 'Step 1: Open the Instagram app on your mobile device.'
                    },
                    {
                        'title': '2. Continue with Facebook',
                        'text': 'Tap "Log in with Facebook" or "Continue as [Your Name]" to sync your account details.',
                        'speech': 'Step 2: Tap Log in with Facebook or Continue to sync your account details.',
                        'images': ['insta_step2.png']
                    },
                    {
                        'title': '3. Enter Your Full Name',
                        'text': 'Type your First Name and Last Name into the name field, then tap Next.',
                        'speech': 'Step 3: Type your First Name and Last Name into the name field, then tap Next.',
                        'images': ['insta_step3.png']
                    },
                    {
                        'title': '4. Create an Easy Username',
                        'text': 'Create a simple username using your first name followed by a number (for example: ram123 or sita45). Tap Next.',
                        'speech': 'Step 4: Create a simple username using your first name followed by a number, such as ram123, then tap Next.',
                        'images': ['insta_step4.png']
                    }
                ]
            },
            'viber': {
                'title': 'Viber Setup Guide',
                'steps': [
                    {
                        'title': '1. Open Viber',
                        'text': 'Open the Viber app and tap "Start Now".',
                        'speech': 'Step 1: Open the Viber app and tap Start Now.',
                        'images': ['viber_step1.png']
                    },
                    {
                        'title': '2. Enter Phone Number',
                        'text': 'Select your country and enter your mobile phone number.',
                        'speech': 'Step 2: Select your country and enter your mobile phone number.',
                        'images': ['viber_step2.png']
                    },
                    {
                        'title': '3. Verify Code',
                        'text': 'Enter the verification code sent to your phone via SMS or phone call.',
                        'speech': 'Step 3: Enter the verification code sent to your phone via SMS or phone call.',
                        'images': ['viber_step3.png']
                    },
                    {
                        'title': '4. Profile Setup',
                        'text': 'Type your First Name and Last Name into the boxes and add a profile photo.',
                        'speech': 'Step 4: Type your First Name and Last Name into the boxes and add a profile photo.',
                        'images': ['viber_step4.png']
                    }
                ]
            },
            'phone': {
                'title': 'Phone & Contacts Guide',
                'steps': [
                    {
                        'title': '1. Enter Phone Number',
                        'text': 'Open the Phone app keypad and type the phone number you want to save.',
                        'speech': 'Step 1: Open the Phone app keypad and type the phone number you want to save.',
                        'images': ['phone_step1.png']
                    },
                    {
                        'title': '2. Click Add Contact',
                        'text': 'Tap "Add Contact" or "Create New Contact" option near the typed number.',
                        'speech': 'Step 2: Tap Add Contact or Create New Contact option near the typed number.',
                        'images': ['phone_step2.png']
                    },
                    {
                        'title': '3. Enter Name',
                        'text': "Type the person's First Name and Last Name into the name fields.",
                        'speech': "Step 3: Type the person's First Name and Last Name into the name fields.",
                        'images': ['phone_step3.png']
                    },
                    {
                        'title': '4. Save Contact',
                        'text': 'Tap "Save" or the Checkmark (✓) icon at the top right to save the number.',
                        'speech': 'Step 4: Tap Save or the checkmark icon at the top right to save the number.'
                    },
                    {
                        'title': '5. Open Recents or Contacts to Block',
                        'text': 'To block someone, go to the "Recents" tab or open your "Contacts" list.',
                        'speech': 'Step 5: To block someone, go to the Recents tab or open your Contacts list.'
                    },
                    {
                        'title': '6. Select Number or Contact',
                        'text': 'Tap the info icon (i) or tap on the contact/number you want to block.',
                        'speech': 'Step 6: Tap the info icon or tap on the contact or number you want to block.'
                    },
                    {
                        'title': '7. Block Contact',
                        'text': 'Scroll to the bottom, tap "Block this Caller" or "Block Contact", and tap confirm.',
                        'speech': 'Step 7: Scroll to the bottom, tap Block this Caller or Block Contact, and tap confirm.'
                    }
                ]
            }
        }
    },
    'np': {
        'nav_home': 'गृहपृष्ठ',
        'nav_guides': 'मार्गदर्शन',
        'switch_lang_code': 'en',
        'switch_lang_btn': '🌐 English',
        'select_app_title': 'एप छान्नुहोस्',
        'search_placeholder': 'एप खोज्नुहोस् (उदा. फेसबुक, ह्वाट्सएप)...',
        'read_aloud_btn': '🔊 विवरण सुन्नुहोस्',
        'back_btn': '⬅ एप सूचीमा फर्कनुहोस्',
        'apps': [
            {'id': 'facebook', 'title': 'फेसबुक र म्यासेन्जर', 'icon': '📘'},
            {'id': 'whatsapp', 'title': 'ह्वाट्सएप', 'icon': '🟢'},
            {'id': 'instagram', 'title': 'इन्स्टाग्राम', 'icon': '📷'},
            {'id': 'viber', 'title': 'भाइबर', 'icon': '💜'},
            {'id': 'phone', 'title': 'फोन र सम्पर्क (Contacts)', 'icon': '📞'}
        ],
        'guides': {
            'facebook': {
                'title': 'फेसबुक तथा म्यासेन्जर प्रयोग गर्ने तरिका',
                'steps': [
                    {
                        'title': '१. नयाँ खाता खोल्नुहोस्',
                        'text': 'फेसबुक एप खोल्नुहोस् र स्क्रिनको मुनि रहेको "Create new account" मा थिच्नुहोस्।',
                        'speech': 'पहिलो चरण: फेसबुक एप खोल्नुहोस् र स्क्रिनको मुनि रहेको नयाँ खाता खोल्नुहोस् मा थिच्नुहोस्।',
                        'images': ['fb_step1_1.png']
                    },
                    {
                        'title': '२. आफ्नो नाम राख्नुहोस्',
                        'text': 'आफ्नो पहिलो नाम र थर टाइप गरेर "Next" मा थिच्नुहोस्।',
                        'speech': 'दोस्रो चरण: आफ्नो पहिलो नाम र थर टाइप गरेर नेक्स्टमा थिच्नुहोस्।',
                        'images': ['fb_step1_2.png']
                    },
                    {
                        'title': '३. जन्ममिति छान्नुहोस्',
                        'text': 'आफ्नो जन्ममिति छानेर "Next" मा थिच्नुहोस्।',
                        'speech': 'तेस्रो चरण: आफ्नो जन्ममिति छानेर नेक्स्टमा थिच्नुहोस्।',
                        'images': ['fb_step1_3.png']
                    },
                    {
                        'title': '४. लिङ्ग छान्नुहोस्',
                        'text': 'आफ्नो लिङ्ग छानेर "Next" मा थिच्नुहोस्।',
                        'speech': 'चौथो चरण: आफ्नो लिङ्ग छानेर नेक्स्टमा थिच्नुहोस्।',
                        'images': ['fb_step1_4.png']
                    },
                    {
                        'title': '५. फोन नम्बर राख्नुहोस्',
                        'text': 'आफ्नो मोबाइल नम्बर राखेर "Next" मा थिच्नुहोस्।',
                        'speech': 'पाँचौँ चरण: आफ्नो मोबाइल नम्बर राखेर नेक्स्टमा थिच्नुहोस्।',
                        'images': ['fb_step1_5.png']
                    },
                    {
                        'title': '६. पासवर्ड बनाउनुहोस्',
                        'text': 'गोप्य पासवर्ड बनाएर "Sign Up" मा थिच्नुहोस्।',
                        'speech': 'छैटौँ चरण: गोप्य पासवर्ड बनाएर साइन अपमा थिच्नुहोस्।',
                        'images': ['fb_step1_6.png']
                    }
                ]
            },
            'whatsapp': {
                'title': 'ह्वाट्सएप प्रयोग गर्ने तरिका',
                'steps': [
                    {
                        'title': '१. ह्वाट्सएप खोल्नुहोस्',
                        'text': 'आफ्नो फोनको होम स्क्रिनबाट ह्वाट्सएप खोल्नुहोस्।',
                        'speech': 'पहिलो चरण: आफ्नो फोनको होम स्क्रिनबाट ह्वाट्सएप खोल्नुहोस्।',
                        'images': ['wa_step1.png']
                    },
                    {
                        'title': '२. सर्तहरू स्वीकार गर्नुहोस्',
                        'text': '"Agree and Continue" मा थिच्नुहोस्।',
                        'speech': 'दोस्रो चरण: एग्री एण्ड कन्टिन्युमा थिच्नुहोस्।',
                        'images': ['wa_step2.png']
                    },
                    {
                        'title': '३. अनुमति (Permissions) दिनुहोस्',
                        'text': 'सम्पर्क (Contacts) र सूचनाहरूका लागि "Allow" मा थिच्नुहोस्।',
                        'speech': 'तेस्रो चरण: सम्पर्क र सूचनाहरूका लागि अलौमा थिच्नुहोस्।'
                    },
                    {
                        'title': '४. फोन नम्बर राख्नुहोस्',
                        'text': 'देश छान्नुहोस् र आफ्नो मोबाइल नम्बर राख्नुहोस्।',
                        'speech': 'चौथो चरण: देश छान्नुहोस् र आफ्नो मोबाइल नम्बर राख्नुहोस्।',
                        'images': ['wa_step4.png']
                    },
                    {
                        'title': '५. नम्बर प्रमाणीकरण गर्नुहोस्',
                        'text': 'मेसेज (SMS) मा आएको ६ अंकको कोड राख्नुहोस्।',
                        'speech': 'पाँचौँ चरण: मेसेजमा आएको ६ अंकको कोड राख्नुहोस्।'
                    },
                    {
                        'title': '६. प्रोफाइल मिलाउनुहोस्',
                        'text': 'आफ्नो नाम राख्नुहोस् र फोटो थप्नुहोस्।',
                        'speech': 'छैटौँ चरण: आफ्नो नाम राख्नुहोस् र फोटो थप्नुहोस्।',
                        'images': ['wa_step6.png']
                    }
                ]
            },
            'instagram': {
                'title': 'इन्स्टाग्राम प्रयोग गर्ने तरिका',
                'steps': [
                    {
                        'title': '१. इन्स्टाग्राम खोल्नुहोस्',
                        'text': 'आफ्नो फोनमा इन्स्टाग्राम एप खोल्नुहोस्।',
                        'speech': 'पहिलो चरण: आफ्नो फोनमा इन्स्टाग्राम एप खोल्नुहोस्।'
                    },
                    {
                        'title': '२. फेसबुकबाट लग इन गर्नुहोस्',
                        'text': '"Log in with Facebook" वा "Continue as..." मा थिचेर फेसबुक खाता जोड्नुहोस्।',
                        'speech': 'दोस्रो चरण: लग इन विथ फेसबुक वा कन्टिन्युमा थिचेर फेसबुक खाता जोड्नुहोस्।',
                        'images': ['insta_step2.png']
                    },
                    {
                        'title': '३. आफ्नो पूरा नाम राख्नुहोस्',
                        'text': 'आफ्नो पहिलो नाम र थर टाइप गर्नुहोस्, त्यसपछि "Next" मा थिच्नुहोस्।',
                        'speech': 'तेस्रो चरण: आफ्नो पहिलो नाम र थर टाइप गर्नुहोस्, त्यसपछि नेक्स्टमा थिच्नुहोस्।',
                        'images': ['insta_step3.png']
                    },
                    {
                        'title': '४. सजिलो युजरनेम (Username) बनाउनुहोस्',
                        'text': 'आफ्नो पहिलो नाम र कुनै अंक मिलाएर सजिलो युजरनेम बनाउनुहोस् (जस्तै: ram123 वा sita45)। त्यसपछि "Next" मा थिच्नुहोस्।',
                        'speech': 'चौथो चरण: आफ्नो पहिलो नाम र अंक मिलाएर सजिलो युजरनेम बनाउनुहोस्, जस्तै राम १२३, त्यसपछि नेक्स्टमा थिच्नुहोस्।',
                        'images': ['insta_step4.png']
                    }
                ]
            },
            'viber': {
                'title': 'भाइबर प्रयोग गर्ने तरिका',
                'steps': [
                    {
                        'title': '१. भाइबर खोल्नुहोस्',
                        'text': 'भाइबर एप खोल्नुहोस् र "Start Now" मा थिच्नुहोस्।',
                        'speech': 'पहिलो चरण: भाइबर एप खोल्नुहोस् र स्टार्ट नाउमा थिच्नुहोस्।',
                        'images': ['viber_step1.png']
                    },
                    {
                        'title': '२. फोन नम्बर राख्नुहोस्',
                        'text': 'आफ्नो मोबाइल नम्बर राखेर "Continue" मा थिच्नुहोस्।',
                        'speech': 'दोस्रो चरण: आफ्नो मोबाइल नम्बर राखेर कन्टिन्युमा थिच्नुहोस्।',
                        'images': ['viber_step2.png']
                    },
                    {
                        'title': '३. कोड प्रमाणीकरण गर्नुहोस्',
                        'text': 'मेसेज वा फोनबाट आएको प्रमाणीकरण कोड राख्नुहोस्।',
                        'speech': 'तेस्रो चरण: मेसेज वा फोनबाट आएको प्रमाणीकरण कोड राख्नुहोस्।',
                        'images': ['viber_step3.png']
                    },
                    {
                        'title': '४. प्रोफाइल मिलाउनुहोस्',
                        'text': 'आफ्नो पूरा नाम (पहिलो नाम र थर) टाइप गर्नुहोस् र फोटो थप्नुहोस्।',
                        'speech': 'चौथो चरण: आफ्नो पूरा नाम टाइप गर्नुहोस् र फोटो थप्नुहोस्।',
                        'images': ['viber_step4.png']
                    }
                ]
            },
            'phone': {
                'title': 'फोन र सम्पर्क प्रयोग गर्ने तरिका',
                'steps': [
                    {
                        'title': '१. फोन नम्बर हाल्नुहोस्',
                        'text': 'फोन एप खोल्नुहोस् र सेभ गर्नुपर्ने नम्बर किपैडमा डायल गर्नुहोस्।',
                        'speech': 'पहिलो चरण: फोन एप खोल्नुहोस् र सेभ गर्नुपर्ने नम्बर किपैडमा डायल गर्नुहोस्।',
                        'images': ['phone_step1.png']
                    },
                    {
                        'title': '२. सम्पर्क थप्नुहोस् मा थिच्नुहोस्',
                        'text': 'नम्बरको नजिकै रहेको "Add Contact" वा "Create New Contact" मा थिच्नुहोस्।',
                        'speech': 'दोस्रो चरण: नम्बरको नजिकै रहेको एड कन्ट्र्याक्ट वा क्रियट न्यू कन्ट्र्याक्टमा थिच्नुहोस्।',
                        'images': ['phone_step2.png']
                    },
                    {
                        'title': '३. नाम टाइप गर्नुहोस्',
                        'text': 'मान्छेको पहिलो नाम र थर सम्बन्धित खाली ठाउँमा राख्नुहोस्।',
                        'speech': 'तेस्रो चरण: मान्छेको पहिलो नाम र थर सम्बन्धित खाली ठाउँमा राख्नुहोस्।',
                        'images': ['phone_step3.png']
                    },
                    {
                        'title': '४. सेभ (Save) गर्नुहोस्',
                        'text': 'माथि दायाँ कुनामा रहेको "Save" वा टिक (✓) चिन्हमा थिचेर नम्बर सेभ गर्नुहोस्।',
                        'speech': 'चौथो चरण: माथि दायाँ कुनामा रहेको सेभ वा टिक चिन्हमा थिचेर नम्बर सेभ गर्नुहोस्।'
                    },
                    {
                        'title': '५. हालैका कल (Recents) वा सम्पर्क सूची खोल्नुहोस्',
                        'text': 'नम्बर ब्लक गर्न "Recents" वा "Contacts" सूची खोल्नुहोस्।',
                        'speech': 'पाँचौँ चरण: नम्बर ब्लक गर्न रिसेन्ट्स वा कन्ट्र्याक्ट्स सूची खोल्नुहोस्।'
                    },
                    {
                        'title': '६. ब्लक गर्नुपर्ने नम्बर छान्नुहोस्',
                        'text': 'ब्लक गर्न चाहेको नम्बर वा नामको (i) आइकन वा नम्बरमा थिच्नुहोस्।',
                        'speech': 'छैटौँ चरण: ब्लक गर्न चाहेको नम्बर वा नामको आइकन वा नम्बरमा थिच्नुहोस्।'
                    },
                    {
                        'title': '७. नम्बर ब्लक (Block) गर्नुहोस्',
                        'text': 'तल सारेर "Block this Caller" वा "Block Contact" मा थिच्नुहोस् र पुष्टि गर्नुहोस्।',
                        'speech': 'सातौँ चरण: तल सारेर ब्लक दिस कसर वा ब्लक कन्ट्र्याक्टमा थिच्नुहोस् र पुष्टि गर्नुहोस्।'
                    }
                ]
            }
        }
    }
}

@app.route('/')
@app.route('/<lang>')
def index(lang='en'):
    if lang not in DATA:
        lang = 'en'
    return render_template('index.html', lang=lang, data=DATA[lang])

@app.route('/apps/<lang>')
def app_list(lang):
    if lang not in DATA:
        lang = 'en'
    return render_template('app_list.html', lang=lang, data=DATA[lang])

@app.route('/guide/<lang>/<app_id>')
def guide(lang, app_id):
    if lang not in DATA or app_id not in DATA[lang]['guides']:
        abort(404)
    guide_info = DATA[lang]['guides'][app_id]
    return render_template('guide.html', lang=lang, data=DATA[lang], guide=guide_info, app_id=app_id)

if __name__ == '__main__':
    app.run(debug=True)