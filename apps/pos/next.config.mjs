/** @type {import('next').NextConfig} */
const nextConfig = {
  transpilePackages: ["@integrated-pos/ui"], // <- important
  experimental: {
    externalDir: true, // helps with monorepos
  },
};
export default nextConfig;
