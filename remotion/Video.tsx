import React from "react";
import {
  AbsoluteFill,
  Img,
  Sequence,
  staticFile,
  interpolate,
  useCurrentFrame,
  spring,
} from "remotion";

import storyboard from "../output/storyboard.json";

const SceneComponent = ({ scene }: any) => {
  const frame = useCurrentFrame();

  const duration = scene.duration * 30;

  // Fade In
  const fadeIn = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Fade Out
  const fadeOut = interpolate(
    frame,
    [duration - 20, duration],
    [1, 0],
    {
      extrapolateLeft: "clamp",
    }
  );

  // Ken Burns Zoom
  const scale = interpolate(
    frame,
    [0, duration],
    [1, 1.12],
    {
      extrapolateRight: "clamp",
    }
  );

  // Slow Pan
  const translateX = interpolate(
    frame,
    [0, duration],
    [0, -50],
    {
      extrapolateRight: "clamp",
    }
  );

  // Caption Animation
  const captionOpacity = spring({
    frame,
    fps: 30,
    config: {
      damping: 18,
    },
  });

  return (
    <AbsoluteFill>

      <Img
        src={staticFile(
          `images/${scene.image_path.split(/[\\/]/).pop()}`
        )}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          opacity: fadeIn * fadeOut,
          transform: `translateX(${translateX}px) scale(${scale})`,
        }}
      />

      {/* Cinematic Overlay */}

      <AbsoluteFill
        style={{
          background:
            "linear-gradient(to top, rgba(0,0,0,0.45), rgba(0,0,0,0.05))",
        }}
      />

      {/* Caption */}

      <div
        style={{
          position: "absolute",
          bottom: 80,
          left: 60,
          right: 60,
          color: "white",
          fontSize: 46,
          fontWeight: "bold",
          textShadow: "0px 3px 18px black",
          opacity: captionOpacity,
          lineHeight: 1.3,
        }}
      >
        {scene.caption}
      </div>

    </AbsoluteFill>
  );
};

export const Video: React.FC = () => {
  let currentFrame = 0;

  return (
    <AbsoluteFill style={{ backgroundColor: "black" }}>
      {storyboard.scenes.map((scene: any, index: number) => {
        const duration = scene.duration * 30;

        const start = currentFrame;

        currentFrame += duration;

        return (
          <Sequence
            key={index}
            from={start}
            durationInFrames={duration}
          >
            <SceneComponent scene={scene} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};