import Image from "next/image";

export default function Hero() {
  return (
    <div>
      <div>
        <h1></h1>
        <p></p>
      </div>
      <Image src="/images/hero.svg" alt="hero" width={500} height={500} />
    </div>
  );
}
