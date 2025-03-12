/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
	  extend: {},
	},
	darkMode: ["class", '[data-theme="dark"]'], // Permite alternar o tema via data-theme
	plugins: [require("@tailwindcss/typography"), require("daisyui")],
	daisyui: {
	  themes: ["light", "dark", "dracula", "autumn"],
	  darkTheme: "dracula",
	  logs: false,
	},
  };
  