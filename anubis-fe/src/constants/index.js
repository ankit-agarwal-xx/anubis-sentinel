import {
  benefitIcon1,
  benefitIcon2,
  benefitIcon3,
  benefitIcon4,
  benefitImage2,
  chromecast,
  disc02,
  discord,
  discordBlack,
  facebook,
  figma,
  file02,
  framer,
  homeSmile,
  instagram,
  notification2,
  notification3,
  notification4,
  notion,
  photoshop,
  plusSquare,
  protopie,
  raindrop,
  recording01,
  recording03,
  roadmap1,
  roadmap2,
  roadmap3,
  roadmap4,
  searchMd,
  slack,
  sliders04,
  telegram,
  twitter,
  yourlogo,
} from "../assets";

export const navigation = [
  {
    id: "0",
    title: "Features",
    url: "#features",
  },
  {
    id: "1",
    title: "Pricing",
    url: "#pricing",
  },
  {
    id: "2",
    title: "How to use",
    url: "#how-to-use",
  },
  {
    id: "3",
    title: "Roadmap",
    url: "#roadmap",
  },
  {
    id: "4",
    title: "New account",
    url: "#signup",
    onlyMobile: true,
  },
  {
    id: "5",
    title: "Sign in",
    url: "#login",
    onlyMobile: true,
  },
];

export const heroIcons = [homeSmile, file02, searchMd, plusSquare];

export const notificationImages = [notification4, notification3, notification2];

export const companyLogos = [yourlogo];

export const brainwaveServices = [
  "Robust Security Analysis",
  "Dynamic Threat Detection",
  "Seamless Integration",
];

export const brainwaveServicesIcons = [
  recording03,
  recording01,
  disc02,
  chromecast,
  sliders04,
];

export const roadmap = [
  {
    id: "0",
    title: "Voice Command Capability",
    text: "Implementing voice recognition features to allow hands-free interaction with the Anubis Sentinel tool. This enhancement would ensure that red teamers can effectively command and control the system without manual input, making the testing process more streamlined and efficient.",
    date: "May 2025",
    status: "coming soon",
    imageUrl: roadmap1,
    colorful: true,
  },
  {
    id: "1",
    title: "Enhanced Security Testing Features",
    text: "Developing comprehensive security testing features, including game-like elements such as badges and leaderboards, to incentivize red teamers to rigorously test for vulnerabilities in RAG LLM systems.",
    date: "May 2025",
    status: "progress",
    imageUrl: roadmap2,
  },
  {
    id: "2",
    title: "Advanced Customization for Red Teamers",
    text: "Providing advanced customization options for red teamers, allowing them to tailor the tool's appearance and behavior for more effective and engaging interaction during security assessments.",
    date: "May 2025",
    status: "progress",
    imageUrl: roadmap3,
  },
  {
    id: "3",
    title: "Integration with Security APIs",
    text: "Enabling integration with various security APIs and external data sources to enrich the testing environment, allowing the tool to simulate more realistic and comprehensive attack scenarios.",
    date: "May 2025",
    status: "done",
    imageUrl: roadmap4,
  },
];

export const collabText =
  "With smart automation and top-notch security, it's the perfect solution for teams looking to work smarter.";

export const collabContent = [
  {
    id: "0",
    title: "Seamless Integration",
    text: collabText,
  },
  {
    id: "1",
    title: "Smart Automation",
  },
  {
    id: "2",
    title: "Top-notch Security",
  },
];

export const collabApps = [
  {
    id: "0",
    title: "Figma",
    icon: figma,
    width: 26,
    height: 36,
  },
  {
    id: "1",
    title: "Notion",
    icon: notion,
    width: 34,
    height: 36,
  },
  {
    id: "2",
    title: "Discord",
    icon: discord,
    width: 36,
    height: 28,
  },
  {
    id: "3",
    title: "Slack",
    icon: slack,
    width: 34,
    height: 35,
  },
  {
    id: "4",
    title: "Photoshop",
    icon: photoshop,
    width: 34,
    height: 34,
  },
  {
    id: "5",
    title: "Protopie",
    icon: protopie,
    width: 34,
    height: 34,
  },
  {
    id: "6",
    title: "Framer",
    icon: framer,
    width: 26,
    height: 34,
  },
  {
    id: "7",
    title: "Raindrop",
    icon: raindrop,
    width: 38,
    height: 32,
  },
];

export const pricing = [
  {
    id: "0",
    title: "Basic",
    description: "Basic red-teaming features for testing LLM security",
    price: "9.99",
    features: [
      "Basic tools for red-teaming your LLM",
      "Prompt injection and hallucination tests",
      "Ability to explore the tool and its features without any cost",
    ],
  },
  {
    id: "1",
    title: "Premium",
    description: "Advanced red-teaming features, priority support, analytics dashboard",
    price: "99.9",
    features: [
      "Advanced tools for comprehensive red-teaming",
      "Detailed analytics dashboard to track tests and results",
      "Priority support to resolve issues quickly",
    ],
  },
  {
    id: "2",
    title: "Enterprise",
    description: "Customizable red-teaming features, advanced analytics, dedicated account management",
    price: null,
    features: [
      "Customizable tools tailored to your LLM security needs",
      "In-depth analytics and reporting",
      "Dedicated account management and support",
    ],
  },
];


export const benefits = [
  {
    id: "0",
    title: "Comprehensive Security Insights",
    text: "Allows users to quickly identify vulnerabilities and security gaps in their LLM systems without sifting through multiple sources.",
    backgroundUrl: "./src/assets/benefits/card-1.svg",
    iconUrl: benefitIcon1,
    imageUrl: benefitImage2,
  },
  {
    id: "1",
    title: "Continuous Improvement",
    text: "Utilizes advanced analytics to understand and address security flaws, providing accurate and actionable insights.",
    backgroundUrl: "./src/assets/benefits/card-2.svg",
    iconUrl: benefitIcon2,
    imageUrl: benefitImage2,
    light: true,
  },
  {
    id: "2",
    title: "Seamless Connectivity",
    text: "Enables secure and convenient access to the Anubis Sentinel tool from any device, ensuring that users can conduct security assessments from anywhere.",
    backgroundUrl: "./src/assets/benefits/card-3.svg",
    iconUrl: benefitIcon3,
    imageUrl: benefitImage2,
  },
  {
    id: "3",
    title: "Rapid Response",
    text: "Facilitates quick identification and resolution of security issues, minimizing the risk of data breaches and unauthorized access.",
    backgroundUrl: "./src/assets/benefits/card-4.svg",
    iconUrl: benefitIcon4,
    imageUrl: benefitImage2,
    light: true,
  },
  {
    id: "4",
    title: "Comprehensive Security Insights",
    text: "Allows users to quickly identify vulnerabilities and security gaps in their LLM systems without sifting through multiple sources.",
    backgroundUrl: "./src/assets/benefits/card-5.svg",
    iconUrl: benefitIcon1,
    imageUrl: benefitImage2,
  },
  {
    id: "5",
    title: "Continuous Improvement",
    text: "Utilizes advanced analytics to understand and address security flaws, providing accurate and actionable insights.",
    backgroundUrl: "./src/assets/benefits/card-6.svg",
    iconUrl: benefitIcon2,
    imageUrl: benefitImage2,
  },
];

export const socials = [
  {
    id: "0",
    title: "Discord",
    iconUrl: discordBlack,
    url: "#",
  },
  {
    id: "1",
    title: "Twitter",
    iconUrl: twitter,
    url: "#",
  },
  {
    id: "2",
    title: "Instagram",
    iconUrl: instagram,
    url: "#",
  },
  {
    id: "3",
    title: "Telegram",
    iconUrl: telegram,
    url: "#",
  },
  {
    id: "4",
    title: "Facebook",
    iconUrl: facebook,
    url: "#",
  },
];
