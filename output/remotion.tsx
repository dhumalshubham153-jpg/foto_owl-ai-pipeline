
/*
=========================================
Retrieved Style Guide
=========================================

Style: Cinematic

Characteristics:
- Slow pacing
- Warm color palette
- Soft fade transitions
- Emotional storytelling
- Minimal captions
- Long scene duration
- Smooth camera movements
- Elegant typography
- Background instrumental music

=========================================
Retrieved Remotion Context
=========================================

Remotion Sequence Component

Purpose:
Controls when an element appears on the timeline.

Example:

<Sequence
    from={0}
    durationInFrames={150}
>

</Sequence>

=========================================
Generated Remotion Composition
=========================================
*/

import { AbsoluteFill, Img, Sequence } from "remotion";

export const WeddingVideo = () => (
  <AbsoluteFill>

    <Sequence from={0} durationInFrames={150}>

      <Img
        src="./images/image_4.jpg.jpg"
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover"
        }}
      />

    </Sequence>

  </AbsoluteFill>
);
