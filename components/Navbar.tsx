"use client";

import * as React from "react";
import Link from "next/link";
import { ModeToggle } from "./theme-switch";
import { Button } from "./ui/button";
import { useState } from "react";
// import { useUser } from "@clerk/nextjs/app-beta/client";
// import { SignOutButton } from "@clerk/nextjs";

import { cn } from "@/lib/utils";
// import { Icons } from "@/components/icons"

export default function Navbar() {
  const [active, setActive] = useState("");

  const handleClick = (elem: string) => {
    setActive(elem);
  };

  //   const { isLoaded, isSignedIn, user } = useUser();

  return (
    <header>
      {/* mobile */}
      {/* <div className="lg:hidden flex">
        <NavigationMenu>
          <NavigationMenuList>
          <NavigationMenuItem className="w-screen flex items-center justify-between px-4 py-2">
            <NavigationMenuItem>
              <Link href="/" legacyBehavior passHref>
                Healthy
              </Link>
            </NavigationMenuItem>
            <NavigationMenuTrigger>
              
            </NavigationMenuTrigger>
            <NavigationMenuContent>

            </NavigationMenuContent>
          </NavigationMenuItem>
          </NavigationMenuList>
        </NavigationMenu>
      </div> */}

      {/* desktop */}
      <div className="w-screen lg:flex hidden border-b dark:border-neutral-800 h-[50px]">
        <nav className="inline-flex items-center justify-between w-full mx-72">
          <ul className="flex items-center">
            <li className="mr-8">
              <Link href="/" className="font-bold text-lg">
                Jobs
              </Link>
            </li>
            <li>
              <Link
                onClick={() => handleClick("find-positions")}
                href="/find-positions"
                className={`hover:text-neutral-600 dark:hover:text-neutral-300 font-semibold text-neutral-500 dark:text-neutral-400 flex w-max items-center justify-center rounded-md my-2 mx-4 text-sm transition-colors ${
                  active === "protein-calculator"
                    ? "dark:text-white"
                    : "text-neutral-400"
                }`}
              >
                Find Positions
              </Link>
            </li>
            <li>
              <Link
                onClick={() => handleClick("about")}
                href="/about"
                className={`hover:text-neutral-600 dark:hover:text-neutral-300 font-semibold text-neutral-500 dark:text-neutral-400 flex w-max items-center justify-center rounded-md my-2 mx-4 text-sm transition-colors ${
                  active === "about" ? "dark:text-white" : "text-neutral-400"
                }`}
              >
                About
              </Link>
            </li>
            <li>
              <Link
                onClick={() => handleClick("faq")}
                href="/faq"
                className={`hover:text-neutral-600 dark:hover:text-neutral-300 font-semibold text-neutral-500 dark:text-neutral-400 flex w-max items-center justify-center rounded-md my-2 mx-4 text-sm transition-colors ${
                  active === "faq" ? "dark:text-white" : "text-neutral-400"
                }`}
              >
                FAQ
              </Link>
            </li>
          </ul>
          <ul className="flex items-center">
            <li className="mr-1">
              <ModeToggle />
            </li>
            <li>
              <Link href="/sign-in" className="mr-1">
                <Button size="sm">Sign in</Button>
              </Link>
            </li>
            <li>
              <Link href="/sign-up">
                <Button variant={"secondary"} size="sm">
                  Sign Up
                </Button>
              </Link>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
}
