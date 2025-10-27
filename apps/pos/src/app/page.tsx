"use client";

import { Button } from "@integrated-pos/ui";

export default function Home() {
  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold mb-4">Web Shop</h1>
      <Button onClick={() => alert("Shared UI works!")}>
        Hello from UI package
      </Button>
    </main>
  );
}
